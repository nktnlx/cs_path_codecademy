import argparse
from tabulate import tabulate  # how to install and use https://pypi.org/project/tabulate/

# parsing optional argument
parser = argparse.ArgumentParser(description='Daily Sales')
parser.add_argument('--filename', help='name of a txt file with data', type=str)
args = parser.parse_args()

# opening and reading file with data
with open(args.filename) as txt_file:
    sales_data = txt_file.read()
    
# replacing delimeter inside one purchase
clean_stage1 = sales_data.replace(';,;', ';').split(',')
clean_stage2 = []
for item in clean_stage1:
    clean_stage2.append(item.split(';'))

# stripping extra spaces
clean_stage3 = []
for purch in clean_stage2:
    for item in purch:
        clean_stage3.append(item.strip())
        
# creating a template for a list with nested lists (each nested list is a single purchase)
purch_list = []
for i in range(len(clean_stage3)//4):
    purch_list.append([])    

# making purchase list with nested purhcases
for empt_lst in purch_list:
    [empt_lst.append(clean_stage3.pop(0).replace('&', ', ')) for _ in range(4)]   

# creating a list of purchase values only
trade_value_lst = []
for purch in purch_list:
    trade_value_lst.append(float(purch[1].replace('$', '')))
    
# creating a list of colors
color_lst = []
for purch in purch_list:
    color_lst.append(purch[2].split(', '))
    
# creating a list of colors (splitting multi-color purchases)
color_lst_split = []
for purch in color_lst:
    if len(purch) <= 1:
        color_lst_split += purch
    if len(purch) > 1:
        color_lst_split.extend(purch)

# making a list of unique colors        
unique_colors = []
for color in color_lst_split:
    if color not in unique_colors:
        unique_colors.append(color)
    
# median value function
def median_value(lst):
    if len(lst) % 2 == 0:
        result = (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    if len(lst) % 2 == 1:
        result = lst[len(lst) // 2]
    return result

# sales day stats
transactions = len(trade_value_lst)
total = sum(trade_value_lst)
min_bill = min(trade_value_lst)
max_bill = max(trade_value_lst)
avg_bill = total / len(trade_value_lst)
median_bill = median_value(sorted(trade_value_lst))

#printing all purchases in tabular view
print(f'\nOpening and reading data from file {args.filename}:')
print(tabulate(purch_list, headers=['Customer', 'Transaction amount', 'Purchase', 'Date'], tablefmt='psql'))

# printing sales stats
print()
print(*'printing sales stats'.upper())
print(f'Date: {purch_list[0][3]}',
      f'Transactions made: {transactions} transactions',
      f'Gross sales: {total:.2f} USD', 
      f'Smallest purchase: {min_bill:.2f} USD', 
      f'Largest purchase: {max_bill:.2f} USD', 
      f'Average purchase: {avg_bill:.2f} USD', 
      f'Median purchase: {median_bill:.2f} USD',
      sep ='\n')

# printing stats on sales by colors
print()
print(*'printing stats on sales by colors'.upper())
for color in unique_colors:
    amount = color_lst_split.count(color)
    print(f'{color.title()} color: {amount} items were sold today.')