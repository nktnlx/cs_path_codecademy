# importing irregular verbs data from irregular_verbs_dict.py (should be in the same folder)
from ppnt_irregular_verbs_dict import irregular_verbs

# importing auxilary verbs data from aux_verbs_dict.py (should be in the same folder)
from aux_verbs_dicts import not_stressed_syllable, irregular_third_person, modal_verbs_singular, modal_verbs_preterite

from tabulate import tabulate  # https://pypi.org/project/tabulate/
import string
import sys


# making a list with punctuation signs to use it later 
# when checkin the proper delimeter
punctuation = []
[punctuation.append(string.punctuation[i]) for i in range(len(string.punctuation))]
punctuation.append(' ')


# greeting a user and making a center alignment for a width of terminal equal 88
greet_txt = 'welcome to \'CONJUGATE ME\'!'.upper()
print('\n')
print(*'{:^44}'.format(greet_txt))
print('\n')


# user input function with check of a proper delimeter in the input
def user_input():
    user_words = input('''Please, enter verbs in infinitive form you\'d like to conjugate and check your grammar.
Verbs should be comma separated (e.g. code, rest, repeat): ''').lower()
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


# following English language rules to form present participle form
def present_participle(lst):
    verb_plus_ing = []
    for word in lst:
        if word in not_stressed_syllable:
            verb_plus_ing.append(word + 'ing')
        elif word in modal_verbs_singular:
            verb_plus_ing.append('-' * len(word))
        elif word[-2:] == 'ie':
            verb_plus_ing.append(word[0:-2] + 'ying')
        elif word[-3:-1] == 'ui' and word [-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'x', 'n']:
            verb_plus_ing.append(word + word[-1:] + 'ing')
        elif word[-1:] == 'e':
            if word in ['be', 'see']:
                verb_plus_ing.append(word + 'ing')
            else:
                verb_plus_ing.append(word[0:-1] + 'ing')
        elif word[-3:-2] in ['a', 'e', 'i', 'o', 'u'] and word[-2:-1] in ['a', 'e', 'i', 'o', 'u'] and word[-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w']:
            verb_plus_ing.append(word + 'ing')
            #continue
        elif word[-2:-1] in ['a', 'e', 'i', 'o', 'u'] and word[-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'x', 'z']:
            verb_plus_ing.append(word + word[-1:] + 'ing')
        else:
            verb_plus_ing.append(word + 'ing')
    return verb_plus_ing


# following English language rules to form third person singular form
def third_person_singular(lst):
    verb_plus_s = []
    for word in lst:
        if word in irregular_third_person:
            verb_plus_s.append(irregular_third_person[word])
        elif word in modal_verbs_singular:
            verb_plus_s.append(modal_verbs_singular[word])
        elif word[-1:] in ['s', 'x', 'z', 'o'] or word[-2:] in ['sh', 'ch']:
            verb_plus_s.append(word + 'es')
        elif word[-1:] == 'y' and word[-2:-1] not in ['a', 'e', 'i', 'o', 'u']:
            verb_plus_s.append(word[0:-1] + 'ies')
        else:
            verb_plus_s.append(word + 's')
    return verb_plus_s


# following English language rules to form past participle form
def past_simple(lst):
    verb_plus_ed = []
    for word in lst:
        if word in modal_verbs_preterite:
            verb_plus_ed.append(modal_verbs_preterite[word])
        elif word in irregular_verbs:
            verb_plus_ed.append(irregular_verbs[word][0])
        elif word in not_stressed_syllable:
            verb_plus_ed.append(word + 'ed')
        elif word[-3:-1] == 'ui' and word [-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'x', 'n']:
            verb_plus_ed.append(word + word[-1:] + 'ed')
        elif word[-2:-1] in ['a', 'e', 'i', 'o', 'u'] and word[-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'x', 'z']:
            verb_plus_ed.append(word + word[-1:] + 'ed')
        elif word[-1:] == 'e':
            verb_plus_ed.append(word + 'd')
        elif word[-1:] == 'y' and word[-2:-1] not in ['a', 'e', 'i', 'o', 'u']:
            verb_plus_ed.append(word[0:-1] + 'ied')
        else:
            verb_plus_ed.append(word + 'ed')
    return verb_plus_ed


# following English language rules to form past participle form
def past_participle(lst):
    verb_plus_ed = []
    for word in lst:
        if word in modal_verbs_preterite:
            if word == 'need':
                verb_plus_ed.append('needed')
            verb_plus_ed.append('-' * len(word))
        elif word in irregular_verbs:
            verb_plus_ed.append(irregular_verbs[word][1])
        elif word in not_stressed_syllable:
            verb_plus_ed.append(word + 'ed')
        elif word[-3:-1] == 'ui' and word [-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'x', 'n']:
            verb_plus_ed.append(word + word[-1:] + 'ed')
        elif word[-2:-1] in ['a', 'e', 'i', 'o', 'u'] and word[-1:] not in ['a', 'e', 'i', 'o', 'u', 'y', 'w', 'x', 'z']:
            verb_plus_ed.append(word + word[-1:] + 'ed')
        elif word[-1:] == 'e':
            verb_plus_ed.append(word + 'd')
        elif word[-1:] == 'y' and word[-2:-1] not in ['a', 'e', 'i', 'o', 'u']:
            verb_plus_ed.append(word[0:-1] + 'ied')
        else:
            verb_plus_ed.append(word + 'ed')
    return verb_plus_ed


# creating an auxilary list with nested lists of verb forms for tabular view 'pretty' print 
def list_of_lists(lst):
    new_lst = [[] for _ in range(len(lst[0]))]
    for item in lst:
        for i in range(len(lst[0])):
            new_lst[i].append(item[i])
    return new_lst


# the main function to run the script with checking for a proper input to exit or continue
def run_the_script():
    answer = '1'
    while answer != '0':
        search_list = user_input()
        result_list = [search_list,
                       third_person_singular(search_list),
                       present_participle(search_list),
                       past_simple(search_list),
                       past_participle(search_list)]
        result_list_print = list_of_lists(result_list)
        print(*'PLEASE, CHECK THE RESULT:')
        print(tabulate(result_list_print, headers=['Infinitive', '3rd Person Singular', 'Present Participle', 'Past Simple', 'Past Participle'], tablefmt='psql'))
        print('-' * len('Press: 1 - for \'YES!\', 0 - for \'EXIT\': '))
        answer = input('''Do you want to check other verbs?
Press: 1 - for 'YES!', 0 - for 'EXIT': ''')
        print('\n')
        while not (answer == '1' or answer == '0'):
                answer = input('''\nDo you want to check other verbs?
Press: 1 - for 'YES!', 0 - for 'EXIT': ''')
        if answer == '0':
            print('Goodbye! If any doubts how to conjugate, come back to check!\n')
            exit()


run_the_script()