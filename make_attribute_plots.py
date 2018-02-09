from __future__ import print_function
import os
import sys
import pathlib
import pandas as pd
import matplotlib

# Check if running on Mac OSX
print('Operating System:', sys.platform)
if sys.platform == 'darwin':
    matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

FILE_NAME = 'water_quality_data.csv'
FOLDER_NAME = 'plots'

def not_found():
    error_string = """\n    Sorry, cannot find the excel file.
    Cannot find {} in the current directory,
    are you running this script in the same directory?.\n"""
    print(error_string.format(FILE_NAME))
    sys.exit(1)

def check_for_graph_dir(folder_name=FOLDER_NAME):
    curr_path = pathlib.Path.cwd()
    graph_path = curr_path / folder_name
    if not graph_path.exists():
        graph_path.mkdir()
        print("""\n{} folder not found in the current directory.
                 Created new folder. Plots will be saved in here.\n
              """.format(folder_name))
    return graph_path.absolute()


def main():

    # Need to use Python 3
    print('Python version:', sys.version)
    print('pandas version:\t', pd.__version__)
    print('matplotlib version:', matplotlib.__version__)

    if sys.version_info <= (3, 5):
        print('Sorry, requires Python 3.5+, not Python 2')
        sys.exit(1)

    # Find CSV file
    cwd = pathlib.Path(os.path.curdir).absolute()
    csv_path = [x for x in cwd.glob('**/{}'.format(FILE_NAME))]

    # Exit if CSV file is not in current directory
    if len(csv_path) == 0:
        not_found()

    # Load CSV file into dataframe
    df = pd.read_csv(str(csv_path[0]), index_col=0)

    # Create folder for plots if it doesn't already exist and get path
    save_path = check_for_graph_dir()

    # Get all station ID's
    sta_ids = [x for x in df['StationUniqueID'].unique()]
    print('Found these stations:\n', str(sta_ids), '\n')

    print('\nEnter 1 if you want to use all stations',
          'or 2 if you want a specific station.')

    user_sta_inp = input()

    while user_sta_inp not in ['1', '2']:
        print('\nInvalid input. Please enter 1 if you want to use all',
              'stations or 2 if you want a specific station.')

        user_sta_inp = input()

    user_sta_inp = int(user_sta_inp)

    if user_sta_inp == 1:
        sta_df = df
        user_sta_id = 'All Stations'
    elif user_sta_inp == 2:
        print('\nIf you know station ID (e.g. "AC01, AC02, etc."),',
              'please enter it. You can also enter multiple stations',
              'separated by a space.')

        user_sta_id = set(input().split())

        while not all(x in sta_ids for x in user_sta_id):
            print('\nPlease choose from the folling ids:\n', *sta_ids)
            user_sta_id = set(input().split())

        sta_df = df[df.StationUniqueID.isin(user_sta_id)]

    # only show parameters with at least this many measurements
    print('\nEnter cutoff number for attribute measurements.',
          'Default is 100 i.e. only show attributes with at least',
          'at least this many number of measurements.')

    cutoff_inp = input()

    try:
        cutoff = int(cutoff_inp)
    except ValueError as ex:
        print('"{}" cannot be converted to an int.'.format(cutoff_inp),
              'Using 100 instead.')
        cutoff = 100

    cnt = sta_df.ParamName.value_counts()
    param_df = sta_df[sta_df.ParamName.isin(cnt.index[cnt.gt(cutoff)])]

    print('\nFound following attributes with {} or more measurements:\n'
          .format(cutoff), param_df.ParamName.unique())

    print('\nEnter parameter to plot. (Use full name)')
    user_param = [input()]

    param_df = sta_df[sta_df.ParamName.isin(user_param)]
    param_df = param_df[['DateCollected', 'Value', 'Units']]

    param_df['DateCollected'] = pd.to_datetime(param_df['DateCollected'],
                                            format='%Y%m%d',
                                            infer_datetime_format=True)

    units = param_df.Units.unique()

    print('\nNumber of missing {} measurements:'
          .format(*user_param), param_df.isnull().sum()[0],
          '\t<-- this number should hopefully be 0.')

    print('\nEnter 1 to plot {} by year.\n'.format(*user_param),
          'Enter 2 to plot by month.\n',
          'Enter 3 to plot by day. \n', sep='')

    user_window = input()
    while user_window not in ['1', '2', '3', '4']:
        print('\nInvalid input. Please enter 1 to plot {} by year.',
              'Enter 2 to plot by month. Enter 3 to plot by day.')

        user_window = input()

    average = True

    if user_window == '1':
        time = 'Year'
        window = 'y'
    elif user_window == '2':
        time = 'Month'
        window = 'm'
    elif user_window == '3':
        time = 'Day'
        window = 'd'

    mod_df = param_df.resample('{}'.format(window),
                            on='DateCollected').mean().dropna(how='all')

    print(mod_df.describe())

    print('\nEnter 1 if you want to view plots.',
          'Enter 2 if you just want to save them.')

    user_view = input()

    while user_view not in ['1', '2']:
        print('\nInvalid input. Please enter 1 to view plots.',
              'Enter 2 if you just want to save them.')

        user_view = input()

    if user_view == '1':
        view_plots = True
    elif user_view == '2':
        view_plots = False

    # Line Plot
    plt.figure(figsize=(20, 5))
    plt.plot(mod_df)
    plt.suptitle('{} {} by {}'.format(user_sta_id, *user_param, time))
    plt.ylabel(units[0])
    plt.savefig(str(save_path / '{}-{}-{}-line-graph'
                    .format(user_sta_id, *user_param, time)))

    if view_plots:
        plt.show()

    # Density Plot
    mod_df.plot(kind='kde', title='{} {} by {}'
                                .format(user_sta_id, *user_param, time))
    plt.xlabel(units[0])
    plt.savefig(str(save_path / '{}-{}-{}-density-graph'
                    .format(user_sta_id, *user_param, time)))
    if view_plots:
        plt.show()

    # Histrogram Plot
    mod_df.plot(kind='hist', title='{} {} by {}'
                                .format(user_sta_id, *user_param, time))
    plt.xlabel(units[0])
    plt.savefig(plt.savefig(str(save_path / '{}-{}-{}-hist-graph'
                    .format(user_sta_id, *user_param, time))))
    if view_plots:
        plt.show()

    print('Done. Saved plots to folder.')

if __name__ == '__main__':
    main()
