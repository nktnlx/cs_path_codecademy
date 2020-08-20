# importing irregular nouns data from irregular_nouns_dict.py (should be in the same folder)
from irregular_nouns_dict import irregular_nouns, nouns_in_plurals

from tabulate import tabulate  # https://pypi.org/project/tabulate/
import string
import sys


# making a list with punctuation signs to use it later 
# when checkin the proper delimeter
punctuation = []
[punctuation.append(string.punctuation[i]) for i in range(len(string.punctuation))]
punctuation.append(' ')


# greeting a user and making a center alignment for a width of terminal equal 88
greet_txt = 'welcome to \'MAKE IT PLURAL\'!'.upper()
print('\n')
print(*'{:^44}'.format(greet_txt))
print('\n')


# user input function with check of a proper delimeter in the input
def user_input():
    user_words = input('''Please, enter nouns in singular form you\'d like to pluralize and check your grammar.
Nouns should be comma separated (e.g. python, code, matrix): ''').lower()
    # checking for the delimeter
    if ', ' not in user_words:

        if user_words[-1:] != ' ':
            for sign in punctuation:
                if sign not in user_words:
                    continue
                else:
                    print('\nPlease, use a comma separated input!')
                    run_the_script()

            # making possible for a single word input to pass the test
            user_words += ', '
            user_list = user_words.split(', ')
            user_list.pop()
            return user_list 

        print('\nPlease, use a comma separated input!')
        run_the_script()
    user_list = user_words.split(', ')

    return user_list


# following English language rules to form plural forms of provided nouns
def plurals(lst):
    lst_with_plurals = []
    for word in lst:
        lst_with_plurals.append(word)
        if word in nouns_in_plurals:
            lst_with_plurals.append(word)
        
        elif word in irregular_nouns:
            lst_with_plurals.append(irregular_nouns[word])
            
        elif word in ['addendum', 'bacterium', 'datum', 'erratum', 'medium']:
            lst_with_plurals.append(word[0:-2] + 'a')
        
        elif word[-2:] == 'us' and word not in ['bus', 'apparatus', 'corpus', 'genus']:
            lst_with_plurals.append(word[0:-2] + 'i')
        
        elif word[-2:] == 'is':
            lst_with_plurals.append(word[0:-2] + 'es')          

        elif word[-2:] == 'on' and word not in ['python']:
            lst_with_plurals.append(word[0:-2] + 'a')      
            
        elif word[-1:] in ['s', 'x', 'z'] or word[-2:] in ['sh', 'ch']:
            if word == 'fez':
                lst_with_plurals.append('fezzes')
                continue
            if word == 'gas':
                lst_with_plurals.append('gasses')
                continue
            lst_with_plurals.append(word + 'es')
            
        elif word[-1:] == 'f':
            exceptions_f = ['roof', 'belief', 'chef', 'chief']
            if word in exceptions_f:
                for item in exceptions_f:
                    if word == item:
                        lst_with_plurals.append(item + 's')
                        break
                continue
            lst_with_plurals.append(word[0:-1] + 'ves')
            
        elif word[-2:] == 'fe':
            lst_with_plurals.append(word[0:-2] + 'ves')
            
        elif word[-1:] == 'y':
            if word[-2:-1] in ['a', 'e', 'i', 'o', 'u']:
                lst_with_plurals.append(word + 's')
                continue
            lst_with_plurals.append(word[0:-1] + 'ies')

        elif word[-1:] == 'o':
            exceptions_o = ['photo', 'piano', 'halo']
            if word in exceptions_o:
                for item in exceptions_o:
                    if word == item:
                        lst_with_plurals.append(item + 's')
                        break
                continue
            lst_with_plurals.append(word + 'es')
            
        else:
            lst_with_plurals.append(word + 's')

    return lst_with_plurals


# creating a auxilary list with nested lists of singular-plural pairs for tabular view 'pretty' print 
def list_of_lists(lst):
    lst_in_lst = [[] for _ in range(len(lst) // 2)]
    for inner_lst in lst_in_lst:
        for i in range(2):
            inner_lst.append(lst[i])
        lst.pop(0)
        lst.pop(0)
    return lst_in_lst


# the main function to run the script with checking for a proper input to exit or continue
def run_the_script():
    answer = '1'
    while answer != '0':
        search_list = user_input()
        result_list = plurals(search_list)
        result_list_print = list_of_lists(result_list)
        print(*'PLEASE, CHECK THE RESULT:')
        print(tabulate(result_list_print, headers=['Singular', 'Plural'], tablefmt='github'))
        print('-' * len('Press: 1 - for \'YES!\', 0 - for \'EXIT\': '))
        answer = input('''Do you want to check other nouns?
Press: 1 - for 'YES!', 0 - for 'EXIT': ''')
        print('\n')
        while not (answer == '1' or answer == '0'):
                answer = input('''\nDo you want to check other nouns?
Press: 1 - for 'YES!', 0 - for 'EXIT': ''')
        if answer == '0':
            print('Goodbye! If any doubts how to pluralize, come back to check!\n')
            exit()


run_the_script()