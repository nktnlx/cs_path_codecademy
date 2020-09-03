# importing irregular nouns data from irregular_nouns_dict.py (should be in the same folder)
from irregular_nouns_dict import irregular_nouns, nouns_in_plurals


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
