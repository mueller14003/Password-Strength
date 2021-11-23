"""
Finds the password strength of an entered password.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from math import ceil, log2

a_size = {"l":26,
          "u":26,
          "n":10,
          "s":30}

symbols = "`~!@#$%^&*()[]{}-_=+\\|;:/?.>,<"

is_symbol = lambda s: s in symbols

def get_type(s):
    return s.isalpha() * (s.islower() * "l" + s.isupper() * "u") + s.isdigit() * "n" + is_symbol(s) * "s"

def get_size(p_word):
    return sum(map(a_size.get, set(map(get_type, p_word))))

def get_combs(p_word):
    return get_size(p_word) ** len(p_word)

def get_bits(p_word):
    return ceil(log2(get_combs(p_word)))

class PasswordStrength(toga.App):
    def startup(self):
        self.placeholder = "password"
        main_box = toga.Box(style=Pack(direction=COLUMN))

        p_word_label = toga.Label(
            'Please enter the password: ',
            style=Pack(padding=(0, 5))
        )
        self.p_word_input = toga.TextInput(style=Pack(flex=1), placeholder=self.placeholder)

        p_word_box = toga.Box(style=Pack(direction=ROW, padding=5))
        p_word_box.add(p_word_label)
        p_word_box.add(self.p_word_input)

        button = toga.Button(
            'Get Password Strength',
            on_press=self.get_password_strength,
            style=Pack(padding=5)
        )

        main_box.add(p_word_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_password_strength(self, widget):
        p_word = self.p_word_input.value or self.placeholder

        self.main_window.info_dialog(
            f"Password Strength for {p_word}",
            f"There are {get_combs(p_word)} combinations\nThat is equivalent to a key of {get_bits(p_word)} bits")

def main():
    return PasswordStrength()
