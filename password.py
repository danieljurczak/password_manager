import random
from string import ascii_uppercase, ascii_lowercase, digits


class Password:
    small_letters = list(ascii_lowercase)
    capital_letters = list(ascii_uppercase)
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '=', '-']
    digits = list(digits)

    def __init__(self, length: int = 16, use_letters: bool = True, use_digits: bool = True,
                 use_special_characters: bool = True, only_capital_letters: bool = False):
        self.length = length
        if not (use_letters or use_digits or use_special_characters):
            raise AttributeError('One of these arguments must be True: use_letters, use_digits, use_special_characters')
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_special_characters = use_special_characters
        self.only_capital_letters = only_capital_letters
        self.password = self.generate_password()

    def __str__(self):
        return self.password

    def __len__(self):
        return self.length

    @property
    def list_of_available_chars(self):
        available_chars = []
        if self.use_letters:
            available_chars += self.capital_letters
        if not self.only_capital_letters:
            available_chars += self.small_letters
        if self.use_digits:
            available_chars += self.digits
        if self.use_special_characters:
            available_chars += self.special_characters

        return available_chars

    def generate_password(self):
        return ''.join(random.choices(self.list_of_available_chars, k=self.length))

