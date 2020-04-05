# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    dict = {
        'password': '',
        'ascii_nums': [48,57],
        'ascii_lower_case': [65,90],
        'ascii_upper_case': [97,122],
    }
    for i in range(4):
        dict['password'] += chr(random.randint(dict['ascii_nums'][0],dict['ascii_nums'][1]))
        dict['password'] += chr(random.randint(dict['ascii_lower_case'][0],dict['ascii_lower_case'][1]))
        dict['password'] += chr(random.randint(dict['ascii_upper_case'][0],dict['ascii_upper_case'][1]))
        dict['password'] += SYMBOLS[random.randint(0,len(SYMBOLS)-1)]

    return dict['password']


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print(f'Insecure Password {password}')


if __name__ == '__main__':
    run()