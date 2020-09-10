The script was coded by me during completion of Codecademy Computer Science Career Path: https://www.codecademy.com/learn/paths/computer-science  


The shipping costs calculator:  
- prints tariffs for different shipping methods in a tabular view  
- takes a weight of a parcel to be shipped from a user input   
- calculates shipping costs for different shipping methods   
- prints the most cost-effective shipping solution for the customer  
- a sample output of running the script is below:  
```
Welcome to the "Fast&Furious" Shipping Agency!
Here is a list of our tariffs:

 G R O U N D   S H I P P I N G
+-----------------+-------------------+
|     Weight      | Price per kg, USD |
+-----------------+-------------------+
| less than 2 kg  |        1.5        |
| from 2 to 6 kg  |        3.0        |
| from 6 to 10 kg |        4.0        |
| 10 kg and more  |       4.75        |
+-----------------+-------------------+
Plus 20.0 USD fix price for the total sum of the tariff.


P R E M I U M   G R O U N D   S H I P P I N G
+-------------------------------------+
| 125.0 USD fix price for any weight! |
+-------------------------------------+


D R O N E   S H I P P I N G
+-----------------+-------------------+
|     Weight      | Price per kg, USD |
+-----------------+-------------------+
| less than 2 kg  |        4.5        |
| from 2 to 6 kg  |        9.0        |
| from 6 to 10 kg |       12.0        |
| 10 kg and more  |       14.25       |
+-----------------+-------------------+


Please, enter the weigth of your parcel in kg and we'll provide you with the cheapest option of the shipment: 7.5

The cheapest option available for a 7.5 kg parcel is 50.00 USD with standard ground shipping.

```


The code was created using Python 3.7.6  
If your machine has an installed Python 3, you can run the code in terminal(command line) by typing:   
$ python3 shipping_costs_calc.py  

To run the script properly, you have to install python-tabulate pretty-print tabular data library (for more info on python-tabulate and how to install it, please, visit https://pypi.org/project/tabulate/):  
$ pip install tabulate  


--------------------------------------------
Fill free to contact me via nktn.lx@gmal.com  
Follow me on twitter: @nktn_lx  
And here on github: github.com/nktnlx  