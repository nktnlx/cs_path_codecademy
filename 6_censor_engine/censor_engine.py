# importing irregular nouns data from irregular_nouns_dict.py (should be in the same folder)
from plurals import plurals

from tabulate import tabulate  # https://pypi.org/project/tabulate/
import argparse
import string
import sys


# parsing optional argument
parser = argparse.ArgumentParser(description='Censor Engine')
parser.add_argument('--filename', help='name of a txt file to censor words/digits in')
args = parser.parse_args()


# opening and reading a text to censor
with open(args.filename) as txt_file:
    input_txt = txt_file.read()


# making a list with punctuation signs to use it later
# when checkin the proper delimeter
punctuation = []
[punctuation.append(string.punctuation[i]) for i in range(len(string.punctuation))]
punctuation.append(' ')


# entering data for censorship with check of a proper delimeter in the input
def user_input():
    user_words = input('''Please, enter words in singular/infinitive form you\'d like to censor.
Words should be comma separated (e.g. fact, check, brother): ''').lower()
    user_sign = input('Please, enter a single sign you\'d like to be used for censoring: ')
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
            return user_list, user_sign

        print('\nPlease, use a comma separated input!')
        run_the_script()
    user_list = user_words.split(', ')

    return user_list, user_sign


#digits = string.digits
#print(digits)

#print(input_txt)
#print(input_txt.replace('cat', '*'*len('cat')))
#txt_as_lst = input_txt.split()
#print(txt_as_lst)


# half of terminal screen width in Ubuntu for proper center alignment
half_width_terminal = 44

# greeting user
def greet():
    print('\n')
    greet = 'welcome to censor engine'.upper()
    print(*'{a:^{b}}'.format(a = greet, b = half_width_terminal))  # center alignment for line width of 124
    print('\n')


# printing original text
def original_txt(text):
    print('\n\n\n' + 'the original text'.upper() + f' (from {args.filename}):')
    print('-' * (half_width_terminal * 2))
    print(text)


# printing words to censor
def print_censor_words(to_censor, sign):
    print('\n')
    print('-' * (half_width_terminal * 2))
    to_censor_string = ', '.join(to_censor)
    print(f'LIST OF WORDS TO BE CENSORED IN THE TEXT: {to_censor_string}')
    print(f'USER DEFINED SIGN TO BE USED FOR CENSORING: {sign}')
    print('-' * (half_width_terminal * 2))
    print('\n')


# printing censored text
def censored_txt(text):
    print('\n' + 'the censored text:'.upper())
    print('-' * (half_width_terminal * 2))
    print(text)


def run_the_script():
    user_words, user_sign = user_input()
    user_words_plurals = plurals(user_words)
    original_txt(input_txt)
    print_censor_words(user_words, user_sign)
    censored_txt(input_txt)
    exit()


greet()
run_the_script()
