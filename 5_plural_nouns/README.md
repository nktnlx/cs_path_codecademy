The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


The 'Make it Plural' script:  
- takes user input of comma separated list of nouns  
- pluralize them according to English language grammar rules  
- uses elif statements and a dictionary of irregular nouns to produce correct plural form  
- the output is pairs of singular -- plural forms of a give noun in a tabular view  
- after the output was printed the program asks to continue with another input or exit  
- a sample output of running the script is below:  
```
 W E L C O M E   T O   ' M A K E   I T   P L U R A L ' !                


Please, enter nouns in singular form you'd like to pluralize and check your grammar.
Nouns should be comma separated (e.g. python, code, matrix): cactus, child, ox, potato, berry

P L E A S E ,   C H E C K   T H E   R E S U L T :
| Singular   | Plural   |
|------------|----------|
| cactus     | cacti    |
| child      | children |
| ox         | oxen     |
| potato     | potatoes |
| berry      | berries  |
---------------------------------------
Do you want to check other nouns?
Press: 1 - for 'YES!', 0 - for 'EXIT': 0


Goodbye! If any doubts how to pluralize, come back to check!

```

The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line) by typing:   
$ python3 plural_nouns.py  

NB! The irregular_nouns_dict.py file (a dictionary of irregular nouns) has to be in the same working directory as the script file to run the program correctly.  


To run the script properly, you have to install python-tabulate pretty-print tabular data library (for more info on python-tabulate and how to install it, please, visit https://pypi.org/project/tabulate/):  
$ pip install tabulate  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  