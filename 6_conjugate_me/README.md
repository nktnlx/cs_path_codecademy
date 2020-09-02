The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


The 'Conjugate Me' script:  
- takes user input of comma separated list of verbs in infinitive form  
- conjugates them according to English language grammar rules  
- uses elif statements and a complete dictionary of 478 irregular verbs to produce correct conjugations  
- the output is in a tabular view, as below:  
+--------------+-----------------------+----------------------+---------------+-------------------+  
| Infinitive   | 3rd Person Singular   | Present Participle   | Past Simple   | Past Participle   |  
|--------------+-----------------------+----------------------+---------------+-------------------|  
| buy          | buys                  | buying               | bought        | bought            |  
| run          | runs                  | running              | ran           | run               |  
| melt         | melts                 | melting              | melted        | melted            |  
+--------------+-----------------------+----------------------+---------------+-------------------+  

- after the output was printed the program asks to continue with another input or exit  


The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line) by typing:   
$ python3 conjugate_verbs.py  

NB! The aux_verbs_dicts.py (a dictionary of auxiliary verbs) and ppnt_irregular_verbs_dict.py (a dictionary of irregular verbs) files have to be in the same working directory as the script file to run the program correctly.  


To run the script properly, you have to install python-tabulate pretty-print tabular data library (for more info on python-tabulate and how to install it, please, visit https://pypi.org/project/tabulate/):  
$ pip install tabulate  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  