# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    dict = {
        'password': '',
        'posibilities': [
            [48, 57],  # numbers
            [65, 90],  # lowercase
            [97, 122],  # uppercase
            [33, 47]  # symbols
        ],
        'countPosibility': [0, 0, 0, 0],
        'pass_all_posibilities': False
    }
    for i in range(16):
        posibility = random.randint(0, 3)

        # Validation check
        if not dict['pass_all_posibilities'] and i > 4:
            index = searchIfExistValue(dict['countPosibility'], 0)
            if index == -1:
                dict['pass_all_posibilities'] = True
            else:
                posibility = index

        dict['countPosibility'][posibility] += 1
        l = dict['posibilities'][posibility]
        dict['password'] += chr(random.randint(l[0], l[len(l)-1]))

    return dict['password']


def searchIfExistValue(list, value):
    try:
        return list.index(value)
    except ValueError:
        return -1


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
        print(f'Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()