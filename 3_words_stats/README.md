The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


words_stats.py:  
- reads a txt file provided as an optional argument when running the script  
- asks whether you want to make a case sensitive or case insensitive search  
- parses the file and calculates frequency of each word occurances  
- prints each word ranked based on its occurance in the text from the most frequent to the least frequent  
- shows the total amount of words in the file   
- a sample output of running the script is below:  
```
WELCOME to 'WORDS STATS'!
Do you want case sensitive statistics?
Press: 1 - for YES; 0 - for NO (make it case insensitive): 0

Case insensitive stats for 'millay_sonnet.txt':
-----------------------------------------------
 1. your      -- appeared 3 times
 2. little    -- appeared 3 times
 3. i         -- appeared 2 times
 4. forget    -- appeared 2 times
 5. or        -- appeared 2 times
 6. shall     -- appeared 1 time
 7. you       -- appeared 1 time
 8. presently -- appeared 1 time
 9. my        -- appeared 1 time
10. dear      -- appeared 1 time
11. so        -- appeared 1 time
12. make      -- appeared 1 time
13. the       -- appeared 1 time
14. most      -- appeared 1 time
15. of        -- appeared 1 time
16. this      -- appeared 1 time
17. day       -- appeared 1 time
18. month     -- appeared 1 time
19. half      -- appeared 1 time
20. a         -- appeared 1 time
21. year      -- appeared 1 time
22. ere       -- appeared 1 time
23. die       -- appeared 1 time
24. move      -- appeared 1 time
25. away      -- appeared 1 time
-----------------------------------------------
The text file has 32 words in it.

```

Optional arguments:  
  -h, --help           show this help message and exit  
  --filename FILENAME  name of a txt file to count symbols  


The directory contains a test txt file to run the script as follows:  
$ python3 words_stats.py --filename=ulysses_chapter_one.txt  

NB! The txt file has to be in the same working directory as the script file.  


The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line) as shown in examples above.    

PS and yes, you can read the first chapter of James Joice 'Ulysses' and even get some insights on the vocabulary and words frequency in this masterpiece of world literature with this repo!    

--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  