def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact does not exist."
        except IndexError:
            return "Provide correct input."
    return wrapper

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise ValueError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all_contacts(args, contacts):
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    commands = {
        "add": add_contact,
        "phone": show_phone,
        "all": show_all_contacts,
    }

    while True:
        command_input = input("Enter a command: ")
        if command_input == "exit":
            print("Goodbye!")
            break
        command, *args = command_input.split()

        if command in commands:
            result = commands[command](args, contacts)
            print(result)
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
