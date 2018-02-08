from __future__ import print_function
import os, sys

FILE_NAME = 'qryDataRequest621OmarA.xlsx'

def not_found():
    error_string = """\n    Sorry, cannot find the excel file.
    Cannot find {} in the current directory,
    are you running this script in the same directory?.\n"""
    sys.stdout.write(error_string.format(FILE_NAME))
    sys.exit(1)


def main():

    # Need to use Python 3
    print('Python version:', sys.version)

    if sys.version_info <= (3, 5):
        sys.stdout.write('Sorry, requires Python 3.5+, not Python 2\n')
        sys.exit(1)
    else:
        import pandas as pd
        import matplotlib
        import pathlib
        print('pandas version:\t', pd.__version__)
        print('matplotlib version:', matplotlib.__version__)

    path = pathlib.Path('.')
    excel_path = [x for x in path.glob('**/{}'.format(FILE_NAME))]

    if len(excel_path) == 0:
        not_found()

    excel_file = str(excel_path[0].absolute())
    df = pd.read_excel(excel_file, index_col=None)
    df.to_csv('water_quality_data.csv', encoding='utf-8')
    # This takes a while...

if __name__ == '__main__':
    main()
