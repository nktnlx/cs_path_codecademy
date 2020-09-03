# importing function to pluralize nouns
from plurals import plurals

# importing functions to conjugate infinitive form of verbs
from conjugate import present_participle, third_person_singular, past_simple, past_participle

from tabulate import tabulate  # https://pypi.org/project/tabulate/
import argparse
import string
import sys


# parsing optional argument
parser = argparse.ArgumentParser(description='Censor Engine')
parser.add_argument('--filename', help='name of a txt file to censor words/digits in')
args = parser.parse_args()


# opening and reading a text file to censor
with open(args.filename) as txt_file:
    input_text = txt_file.read()


# making a list with punctuation signs to use it later
# when checkin the proper delimeter (in user input)
punctuation = []
[punctuation.append(string.punctuation[i]) for i in range(len(string.punctuation))]
punctuation.append(' ')


alphabet = string.ascii_letters


# entering data for censorship with check of a proper delimeter in the input
def user_input():
    user_words = input('''Please, enter words in singular/infinitive form you\'d like to censor.
Words should be comma separated (e.g. fact, check, go): ''').lower()
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


# half of terminal screen width in Ubuntu for proper center alignment of output
half_width_terminal = 48


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


# printing digits to censor
def print_digits(to_censor, sign):
    print('\n')
    print('-' * (half_width_terminal * 2))
    to_censor_string = ', '.join(to_censor)
    print(f'ALL DIGITS WILL BE CENSORED IN THE TEXT: {to_censor_string}')
    print(f'USER DEFINED SIGN TO BE USED FOR CENSORING: {sign}')
    print('-' * (half_width_terminal * 2))
    print('\n')


# unzipping list of lists and removing duplicates to pass the result to censoring_engine()
def unzipping(lst):
    unzipped_lst = []
    for nested_lst in lst:
        for item in nested_lst:
            if isinstance(item, list):
                for word in item:
                    if word not in unzipped_lst:
                        unzipped_lst.append(word)
                continue
            if item not in unzipped_lst:
                unzipped_lst.append(item)

    return unzipped_lst


# censoring text
def censor_engine(text, search_list, repl):
    alphabet = string.ascii_letters
    for word in search_list:
        index = 0
        count = 0
        text_lower = text.lower()
        while index < len(text):
            index = text_lower.find(word) + count
            if index < 0:
                break
            if (text[index:index + len(word)]).lower() == word and text[index + len(word):index + len(word) + 1] not in alphabet and text[index-1:index] not in alphabet:
                text_lower = text_lower[0:index] + text_lower[index:index+len(word)].replace(word, repl * len(word)) + text_lower[index+len(word):]
                text = text[0:index] + text[index:index+len(word)].replace(text[index:index+len(word)], repl * len(word)) + text[index+len(word):]
                count = 0
            else:
                count += 1

    return text


# writing censored text to a file
def write_to_file(file_name, txt):
    with open(file_name[:-4] + '_censored' + '.txt', 'w') as censored_txt:
        censored_txt.write(txt)
    print('\n')
    print('-' * (half_width_terminal * 2))    
    print('WRITING THE CENSORED TEXT TO THE ' + file_name[:-4] + '_censored' + '.txt' + ' FILE IN YOUR WORKING DIRECTORY... DONE!!!')
    print('-' * (half_width_terminal * 2))
    print('\n')


# printing censored text
def censored_txt(text):
    print('\n' + 'the censored text:'.upper())
    print('-' * (half_width_terminal * 2))
    print(text)


# the program runs one of scenarios based on the user choice: substituting words or digits
def run_the_script():
    user_choice = None
    # looping to receive a correct user input (either of two available options)
    while not (user_choice == '1' or user_choice == '0'):
        user_choice = input('''What you would like to censor?
Press: 1 - for 'USER SPECIFIED WORDS', 0 - for 'ALL DIGITS': ''')

        # scenario for substituting user defined words in the text
        if user_choice == '1':
            user_words, user_sign = user_input()

            result_list = [user_words,
                       plurals(user_words),
                       third_person_singular(user_words),
                       present_participle(user_words),
                       past_simple(user_words),
                       past_participle(user_words)]

            final_list = unzipping(result_list)
            original_txt(input_text)
            print_censor_words(user_words, user_sign)
            output_text = censor_engine(input_text, final_list, user_sign)
            censored_txt(output_text)
            write_to_file(args.filename, output_text)
            exit()

        # scenario for substituting all digits in the text
        if user_choice == '0':
            user_words = [str(i) for i in range(10)]
            user_sign = input('Please, enter a single sign you\'d like to be used for censoring: ')
            original_txt(input_text)
            print_digits(user_words, user_sign)
            output_text = censor_engine(input_text, user_words, user_sign)
            censored_txt(output_text)
            write_to_file(args.filename, output_text)
            exit()


greet()
run_the_script()