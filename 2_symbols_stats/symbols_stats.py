import argparse


# parsing optional argument
parser = argparse.ArgumentParser(description='Symbols Stats')
parser.add_argument('--filename', help='name of a txt file to count symbols', type=str)
args = parser.parse_args()


# openning and reading file
with open(args.filename) as txt_file:
    text = txt_file.read()


print('\nWELCOME to \'SYMBOL STATS\'!')


# making a choice to do a case sensitive or case insensitive parsing
text_lst = []
def choice(txt):
    valid_choices = ['0', '1']
    case = input('''Do you want case sensitive statistics?
Press: 1 - for YES; 0 - for NO (make it case insensitive): ''')
    if case in valid_choices:
        if case == '0':
            text_lst.extend(text.lower())
            print(f'\nCase insensitive stats for \'{args.filename}\':')
            return text_lst
        if case == '1':
            text_lst.extend(text)
            print(f'\nCase sensitive stats for \'{args.filename}\':')
            return text_lst
    else:
        choice(text)

        
choice(text)

        
# substituting new line and space symbols
text_lst_upd = []
for char in text_lst:
    if char == '\n':
        char = 'new line symbol'
    if char == ' ':
        char = 'space symbol'
    text_lst_upd.append(char)   


# counting occurances
symb_dict = {}
for symbol in text_lst_upd:
    if symb_dict.get(symbol, 0) == 0:
        symb_dict.update({symbol: text_lst_upd.count(symbol)})

    
# sorting dictionary by value (occurance of a symbol in a descending oreder)
sorted_symb_dict = sorted(symb_dict.items(), key=lambda x: x[1], reverse=True)
  
    
# printing results
print(len(f'Case insensitive stats for \'{args.filename}\':') * '-')
no = 1
for i in sorted_symb_dict:
    if i[1] > 1:
        times = 'times'
    else:
        times = 'time'
    spaces = (len('new line symbol') - len(i[0])) * ' '
    if no <= 9:
        print(f' {no}. {i[0]} {spaces}-- appeared {i[1]} {times}')
    else:
        print(f'{no}. {i[0]} {spaces}-- appeared {i[1]} {times}')
    no += 1
print(len(f'Case insensitive stats for \'{args.filename}\':') * '-')
print(f'The text file has {len(text_lst_upd)} symbols in it.\n')
