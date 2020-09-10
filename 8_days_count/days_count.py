from datetime import datetime, date
import sys


def days_passed():
    today = date.today()
    first_of_jan = date(today.year, 1, 1)
    passed_days = today - first_of_jan
    days_left = first_of_jan.replace(year=today.year + 1) - today
    weeks_passed = passed_days.days // 7
    
    today_str = datetime.strftime(datetime.now(), '%A, %B %d, %Y')
    
    print(f'\nToday {today_str} is Day {passed_days.days + 1} of the year.')
    print(f'{passed_days.days} days have already passed this year.')
    print(f'After today {days_left.days - 1} days are remaining in this year.')
    print(f'YEAR PROGRESS [{weeks_passed / 52 * 100:.0f}%]: ' + '[' + '/' * weeks_passed + '.' * (52 - weeks_passed) + ']')
    

def birthday_input():
    birthday = input('\nPlease, enter your birthday in a valid format (e.g. 17/02/1963): ')
    while not (len(birthday) == 10 and '/' in birthday):
        birthday = input('\nPlease, enter your birthday in a valid format (e.g. 17/02/1963): ')
    birthday_lst = birthday.split('/')
    birthday_lst = [int(i) for i in birthday_lst]
    return birthday_lst


def days_till_birthday(lst):
    day_of_birth, month_of_birth, year_of_birth = lst[0], lst[1], lst[2]
    today = date.today()
    birthday = date(year_of_birth, month_of_birth, day_of_birth)
    birthday_this_year = date(today.year, month_of_birth, day_of_birth)
    
    if birthday > today:
        print('Wow! Congrats! You are from the future!!!'.upper())
    elif birthday_this_year < today:
        age = today.year - birthday.year
        days = today - birthday_this_year
        days_till_bd = birthday.replace(year=today.year + 1) - today
        print(f'You are {age} years and {days.days} days young. Only {days_till_bd.days} days left till your birthday!')
    elif birthday_this_year > today:
        age = today.year - birthday.year
        days = (birthday.replace(year=today.year - 1) - today) * -1
        days_till_bd = birthday_this_year - today
        print(f'You are {age - 1} years and {days.days} days young. Only {days_till_bd.days} days left till your birthday!')

        
    else:
        age = today.year - birthday.year    
        print(f'Congrats! It\'s your birthday! You are {age} years young now.')

        
def greet():
    print(*'WELCOME TO THE \'DAYS COUNT\'\n')
    choice = input('''PRESS:
    1 - for info ABOUT TODAY,
    2 - to count till your Birthday
    Your choice: ''')
    return choice
        
        
def run_the_script(user_input):
    while not (user_input == '1' or user_input == '2'):
        run_the_script(greet())
    if user_input == '1':
        days_passed()
        print('\nGood bye! Please, come back whenever you feel the urge.\n')
        exit()
    elif user_input == '2':
        days_till_birthday(birthday_input())
        print('\nGood bye! Please, come back whenever you feel the urge.\n')
        exit()
    


#birthday_input()

#days_till_birthday(birthday_input())

#days_passed()

run_the_script(greet())