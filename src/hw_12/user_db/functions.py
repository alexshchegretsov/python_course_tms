
import datetime
from time import sleep
from db_functions import (
    read_db,
    refresh_db,
    write_db,
)


def just_press_enter_to_continue():
    input('Press ENTER to continue >>>')


def menu():
    print('\t\t\t\t\t\t\t\t\tversion 1.21 beta')
    print('-' * 55)
    print('\t\t\t\t\t  MENU')
    print('enter the appropriate number to perform the operation')
    print('-' * 55)
    print("""
                1. Create user
                2. Delete user
                3. Show first N users
                4. Search user by id
                5. Edit user data
                6. Filter by keyword
                
                    """)
    print(f'users in database: {len(read_db())}')
    print('-' * 55)
    print('\t\t\t\tFor EXIT enter 0')
    print('-' * 55)


def choose_operation():
    while True:
        operation = input('Enter operation >>>')
        if operation.isdigit() and 0 <= int(operation) < 7:
            return int(operation)
        else:
            print('Enter correct value from 0 to 6')
            sleep(3)
            continue


def create_user():
    first_name = input('Enter first name >>>').title()
    last_name = input('Enter last name >>>').title()
    b_year = int(input('Enter birth year >>'))
    b_month = int(input('Enter birth month >>'))
    b_day = int(input('Enter birth day >>'))
    profession = input('Enter profession >>>')

    new_user = dict(
        first_name=first_name,
        last_name=last_name,
        birth_date=str(datetime.date(b_year, b_month, b_day)),
        profession=profession,
    )
    return new_user


def delete_user():
    data_base = read_db()
    user_id = validation_user_id()
    del data_base[user_id - 1]
    refresh_db(data_base)
    print('Operation completed correctly!')
    sleep(2.5)


def show_n_users():
    data = read_db()
    user_amount = validation_number()
    for index in range(user_amount):
        for k, v in data[index].items():
            print(f'{k}: {v}')
        print('-' * 28)
    just_press_enter_to_continue()


def search_user():
    data_base = read_db()
    user_id = validation_user_id()
    for k, v in data_base[user_id - 1].items():
        print(f'{k}: {v}')
    print('-' * 28)
    just_press_enter_to_continue()


def edit_user():
    data_base = read_db()
    user_id = validation_user_id()
    current_user = data_base.pop(user_id - 1)
    editing_user = {k: input(f'{k,v}  Press ENTER if not change >>>') for (k, v) in current_user.items()}
    for k, v in editing_user.items():
        if not v:
            editing_user[k] = current_user[k]
    data_base.insert(user_id - 1, editing_user)
    refresh_db(data_base)


def filter_by_keyword():
    data_base = read_db()
    keyword = input('Keyword to filter search >>>').title()
    for user in data_base:
        if user['first_name'] == keyword or user['last_name'] == keyword:
            for k, v in user.items():
                print(f'{k}: {v}')
            print('-' * 28)
            just_press_enter_to_continue()
        else:
            print('Nothing found')
            sleep(2.5)


def validation_number():
    length_db = len(read_db())
    while True:
        user_amount = input('Enter number of users >>>')
        print('\n')
        if user_amount.isdigit() and int(user_amount) <= length_db:
            return int(user_amount)
        else:
            print('Enter correct value!')
            sleep(2.5)
            continue


def validation_user_id():
    length_db = len(read_db())
    while True:
        user_id = input('Enter USER id >>>')
        print('-' * 28)
        if user_id.isdigit() and int(user_id) in range(1, length_db + 1):
            return int(user_id)
        else:
            print('Enter correct value!')
            sleep(2.5)
            continue
