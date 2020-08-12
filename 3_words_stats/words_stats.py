import argparse
import string


# parsing optional argument
parser = argparse.ArgumentParser(description='Words Stats')
parser.add_argument('--filename', help='name of a txt file to count symbols', type=str)
args = parser.parse_args()


# openning and reading file
with open(args.filename) as txt_file:
    text = txt_file.read()


# preparing punctuation and digits lists to be removed
not_alpha = []
not_alpha.extend(string.digits)
not_alpha.extend(string.punctuation)
not_alpha += '—'  # appending a special symbol from Ulysses edition
not_alpha.remove('\'')  # adapting for apostrophe


# removing punctuation and digits
def no_punct(text):
    for char in not_alpha:
        text = text.replace(char, ' ')
    return text


# creating a list of words for count
text_lst = no_punct(text).split()


print('\nWELCOME to \'WORDS STATS\'!')


# making a choice to do a case sensitive or case insensitive parsing
text_lst_upd = []
def choice(txt):
    valid_choices = ['0', '1']
    case = input('''Do you want case sensitive statistics?
Press: 1 - for YES; 0 - for NO (make it case insensitive): ''')
    if case in valid_choices:
        if case == '0':
            temp = ' '.join(txt)
            temp_l = temp.lower()
            text_lst_upd = temp_l.split()
            print(f'\nCase insensitive stats for \'{args.filename}\':')
            return text_lst_upd
        if case == '1':
            print(f'\nCase sensitive stats for \'{args.filename}\':')
            text_lst_upd = txt
            return text_lst_upd
    else:
        print('\nPlease, make a valid choice!')
        words_list = choice(text_lst)
        return words_list

 
words_list = choice(text_lst)


#counting occurances
symb_dict = {}
for symbol in words_list:
    if symb_dict.get(symbol, 0) == 0:
        symb_dict.update({symbol: words_list.count(symbol)})

    
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
    spaces = (len(max(words_list, key=len)) - len(i[0])) * ' '
    if no <= 9:
        print(f' {no}. {i[0]} {spaces}-- appeared {i[1]} {times}')
    else:
        print(f'{no}. {i[0]} {spaces}-- appeared {i[1]} {times}')
    no += 1
print(len(f'Case insensitive stats for \'{args.filename}\':') * '-')
print(f'The text file has {len(words_list)} words in it.\n')

