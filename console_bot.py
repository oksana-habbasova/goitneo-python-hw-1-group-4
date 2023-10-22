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

def get_contacts(contacts):
    if len(contacts) == 0:
        return 'There are no saved contacts yet'
    
    contacts_str = ''

    for name, phone in contacts.items():
        contacts_str += f'{name}: {phone}, '
    return contacts_str[:-2]

def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
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
        elif command == 'all':
             print(get_contacts(contacts))
        else:
            print('Invalid command.')

main()