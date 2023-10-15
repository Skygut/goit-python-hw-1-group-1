import commands_function


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = commands_function.parse_input(user_input)
        if command in ["close", "exit", "bye"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(commands_function.show_phone(args, contacts))
        elif command == "all":
            print(commands_function.show_all(args, contacts))
        elif command == "add":
            print(commands_function.add_contact(args, contacts))
        elif command == "change":
            print(commands_function.change_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
