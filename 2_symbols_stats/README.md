The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


symbols_stats.py:  
- reads a txt file provided as an optional argument when running the script  
- asks whether you want to make a case sensitive or case insensitive search  
- parses the file and calculates frequency of each symbol occurances  
- prints each symbol ranked based on its occurance in the text from the most frequent to the least frequent  
- shows the total amount of symbols in the file   
- a sample output of running the script is below:  
```
WELCOME to 'SYMBOL STATS'!
Do you want case sensitive statistics?
Press: 1 - for YES; 0 - for NO (make it case insensitive): 0

Case insensitive stats for 'millay_sonnet.txt':
-----------------------------------------------
 1. space symbol    -- appeared 28 times
 2. e               -- appeared 15 times
 3. o               -- appeared 13 times
 4. t               -- appeared 13 times
 5. r               -- appeared 11 times
 6. l               -- appeared 10 times
 7. a               -- appeared 9 times
 8. y               -- appeared 9 times
 9. ,               -- appeared 9 times
10. i               -- appeared 7 times
11. s               -- appeared 5 times
12. h               -- appeared 5 times
13. m               -- appeared 5 times
14. f               -- appeared 4 times
15. u               -- appeared 4 times
16. new line symbol -- appeared 4 times
17. d               -- appeared 3 times
18. g               -- appeared 2 times
19. n               -- appeared 2 times
20. p               -- appeared 1 time
21. k               -- appeared 1 time
22. v               -- appeared 1 time
23. w               -- appeared 1 time
-----------------------------------------------
The text file has 162 symbols in it.
```

Optional arguments:  
  -h, --help           show this help message and exit  
  --filename FILENAME  name of a txt file to count symbols  


The directory contains a test txt file to run the script as follows:  
$ python3 symbols_stats.py --filename=millay_sonnet.txt  

NB! The txt file has to be in the same working directory as the script file.  


The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line) as shown in examples above.    



--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  