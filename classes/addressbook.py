from collections import UserDict
from dataclasses import dataclass
from datetime import datetime, timedelta
import pickle
from pathlib import Path
from record import Notes, Record, Name, Phone, Email, Birthday, Address, Tag


class Contact_not_found(Exception):
    pass


class MyContactsIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.dictionary[key]
            self.index += 1
            yield key, value
        raise StopIteration


@dataclass
class AddressBook(UserDict):
    def __init__(self):
        self.counter: int
        self.filename = "contacts.bin"
        self.path = Path("./" + self.filename)

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.contacts, file)

    def read_from_file(self):
        if self.path.is_file() == False:
            self.contacts = {
                "Anna Nowak": [
                    "600 123 456", 
                    "anowak@email.com", 
                    "1985-10-20",
                    "",
                    "",
                    "",
                    ],
                "Piotr Wiśniewski": [
                    "512 987 654",
                    "pwiśniewski@email.com",
                    "1992-03-07",
                    "",
                    "",
                    "",
                ],
                "Magdalena Kowalczyk": [
                    "665 111 222",
                    "mkowalczyk@email.com",
                    "1988-07-12",
                    "",
                    "",
                    "",
                ],
                "Kamil Lewandowski": [
                    "700 222 333",
                    "klewandowski@email.com",
                    "1995-01-30",
                    "",
                    "",
                    "",
                ],
                "Aleksandra Wójcik": [
                    "510 333 444", 
                    "awójcik@email.com", 
                    "1983-12-04",
                    "",
                    "",
                    "",
                    ],
                "Michał Kamiński": [
                    "730 444 555", 
                    "mkamiński@email.com", 
                    "1997-09-18",
                    "",
                    "",
                    "",
                    ],
                "Karolina Jankowska": [
                    "602 555 666",
                    "kjankowska@email.com",
                    "1991-06-25",
                    "",
                    "",
                    "",
                ],
                "Tomasz Zając": [
                    "516 666 777", 
                    "tzając@email.com", 
                    "1980-04-09",
                    "",
                    "",
                    "",
                    ],
                "Natalia Szymańska": [
                    "660 777 888",
                    "nszymańska@email.com",
                    "1994-11-19",
                    "",
                    "",
                    "",
                ],
                "Marcin Dąbrowski": [
                    "780 888 999",
                    "mdąbrowski@email.com",
                    "1987-08-03",
                    "",
                    "",
                    "",
                ],
            }
        else:
            with open(self.filename, "rb") as file:
                self.contacts = pickle.load(file)
        return self.contacts

    def __iter__(self):
        return MyContactsIterator(self.contacts)

    def input_error(func):
        def wrapper(*args):
            try:
                return func(*args)
            except KeyError as e:
                print(
                    f"Username not provided or user not found. Try again.\nError details: {str(e)}\n"
                )
            except IndexError as e:
                print(
                    f"Incorrect data has been entered. Try again.\nError details: {str(e)}\n"
                )
            except ValueError as e:
                print(
                    f"I'm sorry, but I don't understand your request. Try again.\nError details: {str(e)}\n"
                )
            except Contact_not_found as e:
                print(f"Contact not found.")
            # except Exception as e:
            #     print(f"Error caught: {e} in function {func.__name__} with values {args}")

        return wrapper

    @input_error
    def check_value(self, value):
        if value is None:
            return ""
        return value

    @input_error
    def func_hello(self):
        print("How can I help you?")

    @input_error
    def func_find(self, name):
        if name in self.contacts:
            print("{:^120}".format("-" * 120))
            print(
                "{:^30}|{:^30}|{:^30}|{:^30}".format(
                    "Name", "Phone", "Email", "Birthday", "Address", "Tag", "Notes"
                )
            )
            print("{:^120}".format("-" * 120))
            print(
                "{:^30}|{:^30}|{:^30}|{:^30}".format(
                    name,
                    self.check_value(self.contacts[name][0]),
                    self.check_value(self.contacts[name][1]),
                    self.check_value(self.contacts[name][2]),
                    self.check_value(self.contacts[name][3]),
                    self.check_value(self.contacts[name][4]),
                    self.check_value(self.contacts[name][5]),
                )
            )
        else:
            raise Contact_not_found

    @input_error
    def func_search(self, keyword):
        print("{:^120}".format("-" * 120))
        print(
            "{:^30}|{:^30}|{:^30}|{:^30}".format(
                "Name", "Phone", "Email", "Birthday", "Address", "Tag", "Notes"
            )
        )
        print("{:^120}".format("-" * 120))
        contact_counter = 0
        for key, value in self.contacts.items():
            if (
                keyword.lower() in key.lower()
                or keyword in value[0]
                or keyword in value[0].replace(" ", "")
                or keyword.lower() in value[1].lower()
                or keyword in value[2]
                or keyword.lower() in value[3].lower() 
                or keyword.lower() in value[4].lower()
                or keyword.lower() in value[5].lower()
            ):
                print(
                    "{:^30}|{:^30}|{:^30}|{:^30}".format(
                        key,
                        self.check_value(self.contacts[key][0]),
                        self.check_value(self.contacts[key][1]),
                        self.check_value(self.contacts[key][2]),
                        self.check_value(self.contacts[key][3]),
                        self.check_value(self.contacts[key][4]),
                        self.check_value(self.contacts[key][5]),
                    )
                )
                contact_counter += 1
        if contact_counter == 0:
            raise Contact_not_found

    @input_error
    def func_show_all(self):
        if not self.contacts:
            print("Address book is empty.")
        else:
            print("{:^140}".format("-" * 140))
            print(
                "{:^30}|{:^20}|{:^30}|{:^20}|{:^40}".format(
                    "Name", "Phone", "Email", "Birthday", "Address"
                )
            )
            print("{:^140}".format("-" * 140))
            for name, contact in self.contacts.items():
                print(
                    "{:^30}|{:^20}|{:^30}|{:^20}|{:^40}".format(
                        name,
                        self.check_value(contact[0]),
                        self.check_value(contact[1]),
                        self.check_value(contact[2]),
                        self.check_value(contact[3]),
                    )
                )

    @input_error
    def func_upcoming_birthdays(self, days_str):
        today = datetime.now()
        formatted_date = today.strftime("%d %B %Y")
        days = int(days_str)
        last_day = today + timedelta(days=days)
        formatted_last_day = last_day.strftime("%d %B %Y")
        print(f"Checking period ({formatted_date} - {formatted_last_day}).")

        birthdays_list = {}
        today_birthday = {}

        for name, user_info in self.contacts.items():
            birthday_str = user_info[2]
            phone = user_info[0]
            email = user_info[1]
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()

            birthday_this_year = birthday.replace(year=today.year)
            birthday_next_year = birthday.replace(year=today.year + 1)

            day_of_week = birthday.strftime("%d %B (%A)")

            if today.date() <= birthday_this_year <= last_day.date() or today.date() <= birthday_next_year <= last_day.date():
                if day_of_week not in birthdays_list:
                    birthdays_list[day_of_week] = []
                birthdays_list[day_of_week].append((name, phone, email))
            elif today.date() == birthday_this_year:
                if day_of_week not in today_birthday:
                    today_birthday[day_of_week] = []
                today_birthday[day_of_week].append((name, phone, email))

        if not any(birthdays_list.values()) and not any(today_birthday.values()):
            print(f"None of your contacts have upcoming birthdays in this period.")
        else:
            print(
                "   O O O O \n"
                "  _|_|_|_|_\n"
                " |         |\n",
                "|         |\n",
                "|_________|\n",
            )
        if any(today_birthday.values()):
            print('Someone has birthday today, so wish "HAPPY BIRTHDAY" today to:')
            print('{:^90}'.format("*"*90))
            print('{:^30}|{:^30}|{:^30}'.format("Name", "Phone", "Email"))
            print('{:^90}'.format("*"*90))
            for day, users in sorted(today_birthday.items(), key=lambda x: x[0]):
                for user_info in users:
                    print("{:^30}|{:^30}|{:^30}".format(*user_info))
                    print('*' * 90)
        if any(birthdays_list.values()):
            print('Send birthday wishes to your contact on the upcoming days:')
            print('{:^120}'.format("-"*120))
            print('{:^30}|{:^30}|{:^30}|{:^30}'.format(
                "Birthday", "Name", "Phone", "Email"))
            print('{:^120}'.format("-"*120))
            for day, users in sorted(birthdays_list.items(), key=lambda x: x[0]):
                for user_info in users:
                    print(
                        "{:^30}|{:^30}|{:^30}|{:^30}".format(
                            day, *user_info
                        )
                    )
                    print('-' * 120)

    @input_error
    def func_show(self, number_of_contacts):
        iterator = iter(self.contacts.items())
        len_of_dictionary = len(list(self.contacts.keys()))
        self.counter = 0
        while True:
            self.counter += 1
            print("\n{:^140}".format("-" * 140))
            print(f"Page {self.counter}")
            print("{:^140}".format("-" * 140))
            print(
                "{:^30}|{:^20}|{:^30}|{:^20}|{:^40}".format(
                    "Name", "Phone", "Email", "Birthday", "Address"
                )
            )
            print("{:^140}".format("-" * 140))
            for _ in range(number_of_contacts):
                try:
                    name, contact = next(iterator)
                    print(
                        "{:^30}|{:^20}|{:^30}|{:^20}|{:^40}".format(
                            name,
                            self.check_value(contact[0]),
                            self.check_value(contact[1]),
                            self.check_value(contact[2]),
                            self.check_value(contact[3]),
                        )
                    )
                except StopIteration:
                    break
            print("{:^140}".format("-" * 140))
            if self.counter * number_of_contacts < len_of_dictionary:
                choice = input(
                    f"Do you want to display next {number_of_contacts} contact(s)? (Y/N) "
                )
                if choice not in ["y", "Y", "Yes", "yes", "True"]:
                    break
            else:
                break

    @input_error
    def func_add(self, name, phone=None, address=None, email=None, birthday=None, tag=None, notes=None):
        if len(name) == 0:
            raise KeyError
        else:
            new_contact = Record(
                Name(name),
                Phone(phone),
                Email(email),
                Birthday(birthday),
                Address(address),
                Tag(tag),
                Notes(notes)
            )
            self.contacts[new_contact.name.value] = [
                new_contact.phone.value,
                new_contact.email.value,
                new_contact.birthday.value,
                new_contact.address.value,
                new_contact.tag.value,
                new_contact.notes.value
            ]
            print("{:^140}".format("-" * 140))
            print(
                "{:^30}|{:^20}|{:^30}|{:^20}|{:^40}".format(
                    "Name", "Phone", "Email", "Birthday", "Address"
                )
            )
            print("{:^140}".format("-" * 140))
            print(
                "{:^30}|{:^20}|{:^30}|{:^20}|{:^40}".format(
                    name,
                    self.check_value(self.contacts[name][0]),
                    self.check_value(self.contacts[name][1]),
                    self.check_value(self.contacts[name][2]),
                    self.check_value(self.contacts[name][3]),
                )
            )

    @input_error
    def func_birthday(self, name):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.days_to_birthday(contact.name, contact.birthday)
        else:
            raise Contact_not_found

    @input_error
    def func_edit_phone(self, name, new_phone):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.edit_phone(Phone(new_phone)._value)
            self.contacts[contact.name][0] = contact.phone
        else:
            raise Contact_not_found

    @input_error
    def func_edit_email(self, name, new_email):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.edit_email(new_email)
            self.contacts[contact.name][1] = contact.email
        else:
            raise Contact_not_found

    @input_error
    def func_edit_birthday(self, name, new_birthday):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.edit_birthday(Birthday(new_birthday)._value)
            self.contacts[contact.name][2] = contact.birthday
        else:
            raise Contact_not_found

    @input_error
    def func_delete_contact(self, name):
        if name in self.contacts:
            self.contacts.pop(name)
            print("Contact deleted.")
        else:
            raise Contact_not_found

    @input_error
    def func_delete_phone(self, name):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.delete_phone()
            self.contacts[contact.name][0] = contact.phone
        else:
            raise Contact_not_found

    @input_error
    def func_delete_email(self, name):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.delete_email()
            self.contacts[contact.name][1] = contact.email
        else:
            raise Contact_not_found

    @input_error
    def func_delete_birthday(self, name):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.delete_birthday()
            self.contacts[contact.name][2] = contact.birthday
        else:
            raise Contact_not_found

    @input_error
    def func_edit_address(self, name, new_address):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.edit_address(Address(new_address)._value)
            # Aktualizacja adresu
            self.contacts[contact.name][3] = contact.address
        else:
            raise Contact_not_found

    @input_error
    def func_delete_address(self, name):
        if name in self.contacts:
            contact = Record(
                name,
                self.contacts[name][0],
                self.contacts[name][1],
                self.contacts[name][2],
                self.contacts[name][3],
                self.contacts[name][4],
                self.contacts[name][5],
            )
            contact.delete_address()
            # Usunięcie adresu
            self.contacts[contact.name][3] = contact.address
        else:
            raise Contact_not_found

    @input_error
    def func_exit(self):
        print("Good bye!\n")
        exit()
