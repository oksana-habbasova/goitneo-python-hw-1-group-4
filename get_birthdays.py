from datetime import datetime
from collections import defaultdict

# def get_birthdays_per_week(users):

#     next_week_birthdays = defaultdict(list)

#     today = datetime.today().date()

#     for user in users:
#         name = user['name']
#         birthday = user['birthday'].date()
#         birthday_this_year = birthday.replace(year=today.year)

#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year=today.year + 1)

#         delta_days = (birthday_this_year - today).days

#         if delta_days < 7:
#             day = birthday_this_year.strftime('%A')

#             if day == 'Saturday' or day == 'Sunday':
#                 day = 'Monday'

#             next_week_birthdays[day].append(name)

#     for day, names in next_week_birthdays.items():
#         print(day + ': ' + ', '.join(names))


# ----------------------------------


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact changed.'

def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        print(contacts)

        if command in ['close', 'exit', 'good bye']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_phone(args, contacts))
        else:
            print('Invalid command.')

main()