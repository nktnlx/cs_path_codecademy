# importing irregular verbs data from irregular_verbs_dict.py (should be in the same folder)
from irregular_verbs_dict import irregular_verbs

# importing auxilary verbs data from aux_verbs_dict.py (should be in the same folder)
from aux_verbs_dicts import not_stressed_syllable, irregular_third_person, modal_verbs_singular, modal_verbs_preterite


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
        if word == 'be':
            verb_plus_s.append('am')  # duct taping first person singular for 'be'
            verb_plus_s.append('are')  # duct taping first person plural for 'be'
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