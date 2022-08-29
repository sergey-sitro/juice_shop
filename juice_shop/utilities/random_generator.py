import random
import string


def generate_random_symbols():
    random_symbols = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(12)])
    return random_symbols
