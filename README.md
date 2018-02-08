# README

### Package Dependencies
* `Python 3.5` version or greater
* `matplotlib`
* `pandas`
I _highly_ recommend installing the [Anaconda](https://conda.io/docs/user-guide/install/index.html) distribution of Python and installing all dependencies using [Conda Package Manager](https://conda.io/docs/). It's the easiest way to install Python packages and you don't need root or administrator privileges to use it.


### To Run Scripts
1. Make sure you have all the dependencies installed.
2. Open up `cmd` if on Windows and `terminal` if on Mac OSX
3. Convert the excel file `qryDataRequest621OmarA.xlsx` to CSV format by using `python convert_convert_excel_to_csv.py` (make sure that you run the script in the same directory folder as the excel file).
4. Run `python make_attribute_plots.py` and follow the instructions in the command prompt to customize what kind of plot and attribute you want (make sure to run this script in the same directory folder as the csv file.
5. The script will save 3 plots (line, density, histogram) in a folder called `plots` (this folder will be created if it does not already exist)


### Common Issues
* Make sure you are using Python 3.5+ instead of Python 2 when running the scripts.
* Make sure `matplotlib` and `pandas` are installed before running the scripts. If you are using the Conda package manager you can easily install these dependencies by running the commands `conda install matplotlib` and `conda install pandas` in the command prompt.
* If you are still having issues, feel free to please email me at clu2033@gmail.com. Please include information the operating system, Python version, and versions of Matplotlib and Pandas (You can find this information in the console print out when running a script).


### MIT Licence
Copyright 2018 Charles Lu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
