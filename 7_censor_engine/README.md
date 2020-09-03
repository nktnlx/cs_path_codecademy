
The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


The 'Censor Engine' script:  
- reads a text file  
- asks a user which words (or set of digits) to be replaced  
- pluralizes user specified nouns  
- conjugates user defined verbs  
- replaces all their (user specified nouns and verbs) forms by a user defined symbol in the text read from a file  
- prints out the censored text with all the substitutions made  
- writes it into a new file in the working directory  
- the result of running the script with *my_file.txt* is as below:


```
                        W E L C O M E   T O   C E N S O R   E N G I N E                        

What you would like to censor?
Press: 1 - for 'USER SPECIFIED WORDS', 0 - for 'ALL DIGITS': 1
Please, enter words in singular/infinitive form you'd like to censor.
Words should be comma separated (e.g. fact, check, go): censorship, can, be, control
Please, enter a single sign you'd like to be used for censoring: *


THE ORIGINAL TEXT (from my_file.txt):
------------------------------------------------------------------------------------------------
https://en.wikipedia.org/wiki/Censorship

Censorship is the suppression of speech, public communication, or other information, on the basis
that such material is considered objectionable, harmful, sensitive, or "inconvenient." Censorship
can be conducted by governments, private institutions, and other controlling bodies. 
Direct censorship may or may not be legal, depending on the type, location, and content. Many
countries provide strong protections against censorship by law, but none of these protections are
absolute and frequently a claim of necessity to balance conflicting rights is made, in order to
determine what could and could not be censored.


------------------------------------------------------------------------------------------------
LIST OF WORDS TO BE CENSORED IN THE TEXT: censorship, can, be, control
USER DEFINED SIGN TO BE USED FOR CENSORING: *
------------------------------------------------------------------------------------------------


THE CENSORED TEXT:
------------------------------------------------------------------------------------------------
https://en.wikipedia.org/wiki/**********

********** ** the suppression of speech, public communication, or other information, on the basis
that such material ** considered objectionable, harmful, sensitive, or "inconvenient." **********
*** ** conducted by governments, private institutions, and other *********** bodies. 
Direct ********** may or may not ** legal, depending on the type, location, and content. Many
countries provide strong protections against ********** by law, but none of these protections ***
absolute and frequently a claim of necessity to balance conflicting rights ** made, in order to
determine what ***** and ***** not ** censored.


------------------------------------------------------------------------------------------------
WRITING THE CENSORED TEXT TO THE my_file_censored.txt FILE IN YOUR WORKING DIRECTORY... DONE!!!
------------------------------------------------------------------------------------------------

```


Optional arguments:  
  -h, --help           show this help message and exit  
  --filename FILENAME  name of a txt file to count symbols  


The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line).  
The directory contains a txt file with a text sample to run the script as follows:
$ python3 censor_engine.py --filename=my_file.txt  


NB! The txt file has to be in the same working directory as the script file.  
The result of running the script is in my_file_censored.txt  


NB! The aux_verbs_dicts.py, conjugate.py, irregular_nouns_dict.py, irregular_verbs_dict.py and plurals.py files have to be in the same working directory as the script file to run the program correctly.  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  