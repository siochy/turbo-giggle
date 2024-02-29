import random
import string


def generate_random_text():
    rand_symbols = string.printable
    rand_text = ''.join(random.choice(rand_symbols) for i in range(random.randint(1000, 5000)))
    rand_text_bin = rand_text.encode('utf-8')
    with open('some_text.bin', 'wb') as file:
        file.write(rand_text_bin)


def reading_bin_file():
    with open('some_text.bin', 'rb') as file:
        text_from_file_bin = file.readlines()
        symbols = 0
        words = 0
        lines = len(text_from_file_bin)
        for line in text_from_file_bin:
            symbols += len(line.decode('utf-8'))
            words += len(line.decode('utf-8').split())
        file.seek(0)
        text_from_file_str = file.read().decode('utf-8')

    print(f'Text from file:\n{text_from_file_str}')
    print(f'Symbols: {symbols}')
    print(f'Words: {words}')
    print(f'Lines: {lines}')


generate_random_text()
reading_bin_file()
