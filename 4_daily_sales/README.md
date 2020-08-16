The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


The Daily Sales calculator:  
- reads a txt file provided as an optional argument when running the script  
- cleans imported data  
- prints sales data in a tabular view  
- calculates and prints daily sales statistics (total number of transactions, gross sales, smallest purchase, largest purchase, average purchase, median purchase)   
- calculates and prints sales stats by colors of sold items  


Optional arguments:  
  -h, --help           show this help message and exit  
  --filename FILENAME  name of a txt file to count symbols  


The directory contains a txt file with sales data to run the script as follows:  
$ python3 daily_sales.py --filename=170915_sales_data.txt  

NB! The txt file has to be in the same working directory as the script file.  


The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line) as shown in examples above.    


To run the script properly, you have to install python-tabulate pretty-print tabular data library (for more info on python-tabulate and how to install it, please, visit https://pypi.org/project/tabulate/):  
$ pip install tabulate  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  