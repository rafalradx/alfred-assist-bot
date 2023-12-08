from addressbook import AddressBook


def clossest_match(querry: str, commands):
    """filters commands if they start with querry,
    if no command found querry is shortened by one char from the end
    and function tries again (recursively)"""
    if len(querry) == 0:
        return []
    matched_commands = list(filter(lambda x: x.startswith(querry), commands))
    if len(matched_commands) > 0:
        return matched_commands
    else:
        return clossest_match(querry[:-1], commands)


def command_hint(user_str: str, commands) -> str:
    """return string with hint for user describing
    closest match to the available bot commands"""
    user_str = user_str.strip()
    hint = ""
    hits = clossest_match(user_str, commands)

    if len(hits) > 0:
        hint = f"Did you mean?: {', '.join(hits)}"
    return hint


def main():
    print(
        """
Hello! I am your virtual assistant.
What would you like to do with your Address Book?
Choose one of the commands:
    - hello - let's say hello,
    - find - to find a contact by name,
    - search - to find a contact after entering keyword,
    - show all - to show all of your contacts from address book,
    - show - to display N contacts from Address Book,
    - add - to add new contact to Address Book,
    - birthday - to display days to birthday of the user,
    - edit phone - to change phone of the user,
    - edit email - to change email of the user,
    - edit birthday - to change birthday of the user,      
    - delete contact - to remove contact from Address Book
    - delete phone - to delete phone of the user,
    - delete email - to delete email of the user,
    - delete birthday - to delete birthday of the user,
    - good bye, close, exit or . - to say good bye and close the program.
After entering the command, you will be asked for additional information if needed to complete the command."""
    )
    addressbook = AddressBook()
    addressbook.read_from_file()
    OPERATIONS_MAP = {
        "hello": addressbook.func_hello,
        "find": addressbook.func_find,
        "search": addressbook.func_search,
        "show all": addressbook.func_show_all,
        "show": addressbook.func_show,
        "add": addressbook.func_add,
        "birthday": addressbook.func_birthday,
        "edit phone": addressbook.func_edit_phone,
        "edit email": addressbook.func_edit_email,
        "edit birthday": addressbook.func_edit_birthday,
        "edit address": addressbook.func_edit_address,
        "delete contact": addressbook.func_delete_contact,
        "delete phone": addressbook.func_delete_phone,
        "delete email": addressbook.func_delete_email,
        "delete birthday": addressbook.func_delete_birthday,
        "delete address": addressbook.func_delete_address,
        "good bye": addressbook.func_exit,
        "close": addressbook.func_exit,
        "exit": addressbook.func_exit,
        ".": addressbook.func_exit,
    }
    while True:
        listen_enterred = input("\nEnter your command here: ")
        listen = listen_enterred.lower()
        if listen in OPERATIONS_MAP:
            if listen == "add":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                birthday = input("Enter birthday: ")
                address = input("Enter address:")
                tag = input("Enter tag: ") 
                notes = input("Enter your notes: ")
                OPERATIONS_MAP[listen](name, phone, email, birthday, address, tag, notes)
            elif listen in [
                "find",
                "birthday",
                "delete contact",
                "delete phone",
                "delete email",
                "delete birthday",
                "delete address",
            ]:
                name = input("Enter name: ")
                OPERATIONS_MAP[listen](name)
            elif listen == "search":
                keyword = input("Enter keyword: ")
                OPERATIONS_MAP[listen](keyword)
            elif listen == "edit phone":
                name = input("Enter name of the contact to edit phone: ")
                new_phone = input("Enter new phone number: ")
                OPERATIONS_MAP[listen](name, new_phone)
            elif listen == "edit email":
                name = input("Enter name of the contact to edit email: ")
                new_email = input("Enter new email: ")
                OPERATIONS_MAP[listen](name, new_email)
            elif listen == "edit birthday":
                name = input("Enter name of the contact to edit birthday: ")
                new_birthday = input("Enter new birthday: ")
                OPERATIONS_MAP[listen](name, new_birthday)
            elif listen == "show":
                number_of_contacts = int(input("Enter number of contacts to display: "))
                OPERATIONS_MAP[listen](number_of_contacts)
            elif listen in ["good bye", "close", "exit", "."]:
                addressbook.save_to_file()
                OPERATIONS_MAP[listen.lower()]()
            else:
                OPERATIONS_MAP[listen.lower()]()
        else:
            hint_for_user = command_hint(listen, OPERATIONS_MAP.keys())
            if hint_for_user:  # not empty string
                print(hint_for_user)
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
