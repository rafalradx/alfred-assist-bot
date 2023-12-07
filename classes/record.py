from dataclasses import dataclass
import re
from datetime import datetime


@dataclass
class Field:
    value: str = None


@dataclass
class Name(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


@dataclass
class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value is not None and not self.validate_phone(new_value):
            raise ValueError("Invalid phone number format")
        self._value = new_value

    def validate_phone(self, value):
        if len(value) == 0:
            return True
        if value is not None:
            validate_regex = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
            if re.match(validate_regex, value):
                return True
        return False


@dataclass
class Email(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


@dataclass
class Birthday(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value is not None and not self.validate_birthday(new_value):
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        self._value = new_value

    def validate_birthday(self, value):
        date_format = "%Y-%m-%d"
        if len(value) == 0:
            return True
        try:
            datetime.strptime(value, date_format)
            return True
        except:
            return False


@dataclass
class Record:
    name: Name
    phone: Phone
    email: Email
    birthday: Birthday

    def edit_phone(self, new_phone):
        self.phone = new_phone
        print(f"Phone number updated for {self.name}")

    def edit_email(self, new_email):
        self.email = new_email
        print(f"Email updated for {self.name}")

    def edit_birthday(self, new_birthday):
        self.birthday = new_birthday
        print(f"Birthday updated for {self.name}")

    def delete_phone(self):
        self.phone = None
        print(f"Phone number deleted for {self.name}")

    def delete_email(self):
        self.email = None
        print(f"Email deleted for {self.name}")

    def delete_birthday(self):
        self.birthday = None
        print(f"Birthday deleted for {self.name}")

    def days_to_birthday(self, contact_name, contact_birthday):
        if contact_birthday is not None and len(contact_birthday) > 0:
            current_datetime = datetime.now()
            birthday_strptime = datetime.strptime(contact_birthday, "%Y-%m-%d")
            birthday_date = datetime(
                current_datetime.year, birthday_strptime.month, birthday_strptime.day
            )
            if current_datetime.date() == birthday_date.date():
                print(f"Today is {contact_name}'s birthday!")
            else:
                if current_datetime.date() > birthday_date.date():
                    birthday_date = datetime(
                        current_datetime.year + 1,
                        birthday_strptime.month,
                        birthday_strptime.day,
                    )
                to_birthday = (birthday_date - current_datetime).days
                print(f"Days until {contact_name}'s birthday: {to_birthday}")
        else:
            print(f"{contact_name} has no birthday entered in the address book.")
