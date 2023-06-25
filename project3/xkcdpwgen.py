#! /usr/bin/env python3
import argparse
import random

# Default wordlist file
WORDLIST_FILE = 'words.txt'


def load_wordlist(file):
    with open(file, 'r') as f:
        return [word.strip() for word in f]


def generate_password(words, capitalize, numbers, symbols):
    wordlist = load_wordlist(WORDLIST_FILE)
    password_words = random.choices(wordlist, k=words)

    if capitalize > 0:
        password_words = [
            word.capitalize() if random.choice([True, False]) else word
            for word in password_words
        ]


    for _ in range(numbers):
        index = random.randint(0, len(password_words))
        password_words.insert(index, str(random.randint(0, 9)))


    symbols_list = '~!@#$%^&*.:;'
    for _ in range(symbols):
        index = random.randint(0, len(password_words))
        password_words.insert(index, random.choice(symbols_list))

    return ''.join(password_words)


def main():
    parser = argparse.ArgumentParser(
        description='Generate a secure, memorable password using the XKCD method'
    )
    parser.add_argument('-w', '--words', type=int, default=4,
                        help='include WORDS words in the password (default=4)')
    parser.add_argument('-c', '--caps', type=int, default=0,
                        help='capitalize the first letter of CAPS random words (default=0)')
    parser.add_argument('-n', '--numbers', type=int, default=0,
                        help='insert NUMBERS random numbers in the password (default=0)')
    parser.add_argument('-s', '--symbols', type=int, default=0,
                        help='insert SYMBOLS random symbols in the password (default=0)')
    args = parser.parse_args()

    password = generate_password(args.words, args.caps, args.numbers, args.symbols)
    print(password)


if __name__ == '__main__':
    main()
