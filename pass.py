import random
import string

def generate_password(length):
    possible_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(possible_chars) for i in range(length))
    return password


if __name__ == '__main__':
    length = 16
    print(generate_password(length))
    

    