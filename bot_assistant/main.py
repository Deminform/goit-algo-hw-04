import re
import uuid
from colorama import Fore, Style, init


def main():
    contacts = []
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        init(autoreset=True)

        if command in ['close', 'exit']:
            print("Good bye!")
            break
        elif command in ['hello', 'hi']:
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print(Fore.YELLOW + 'Invalid command.')


# Parsing the input command
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Add person
def add_contact(args: list, contacts: list):
    if len(args) != 2:
        return Fore.YELLOW + 'Incorrect format. Enter in format' + Style.BRIGHT + ' "command Name Phone".'

    name, phone = args
    if not is_valid_phone_number(phone):
        return Fore.YELLOW + 'Incorrect phone number.'

    if not is_person_exist(name, contacts):
        contacts.append({
            'id': str(uuid.uuid4()),
            'name': name,
            'phone': phone})
        return Fore.GREEN + 'Contact added.'
    else:
        return Fore.YELLOW + 'Username already taken.'


# Change phone by name
def change_contact(args: list, contacts: list):
    if len(args) != 2:
        return Fore.YELLOW + 'Incorrect format. Enter in format' + Style.BRIGHT + ' "command Name Phone".'

    name, phone = args
    if not is_valid_phone_number(phone):
        return Fore.YELLOW + 'Incorrect phone number.'

    if is_person_exist(name, contacts):
        for person in contacts:
            if person['name'].lower() == name.lower():
                person['phone'] = phone
                return Fore.GREEN + 'Contact updated.'
    return Fore.YELLOW + 'Username not found.'


# Get the phone by name
def show_phone(args: list, contacts: list):
    if not args:
        return Fore.YELLOW + 'Please type a' + Style.BRIGHT + ' Username'

    for person in contacts:
        if person['name'].lower() == args[0].lower():
            return person['phone']
    return Fore.YELLOW + 'Username not found.'


# Find person by name
def is_person_exist(name: str,  contacts: list) -> bool:
    for person in contacts:
        if person['name'].lower() == name.lower():
            return True


def is_valid_phone_number(phone: str) -> bool:
    return bool(re.match(r'^\+?1?\d{9,13}$', phone))


def show_all(contacts: list) -> str:
    persons_list = ''
    for person in contacts:
        persons_list += (
            f'Name: {person['name']}, '
            f'Phone: {person['phone']}, '
            f'id: {person["id"]}.\n'
        )
    return Fore.YELLOW + 'No records yet' if len(contacts) == 0 else persons_list


if __name__ == '__main__':
    main()
