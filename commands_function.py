def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


def add_contact(args, contacts):
    if not validate_args(args):
        return "Enter corect arguments!"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if not validate_args(args):
        return "Enter corect number!"
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} not exists."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Enter corect Name!"
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        return phone
    else:
        return f"{name} not exists"


def show_all(args, contacts):
    if len(args) != 0:
        return "Not right command all!"
    return contacts
