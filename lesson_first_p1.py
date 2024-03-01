import random
import string


def generate_random_text():
    """Generates text for binary file.
    Takes symbols 'a..Z', '0..9', '!..+' and spaces.
    Then encodes this with utf-8 and write into the .bin file
    'some_text.bin'.
    Uses for tests. You can take your own text in some_text.bin file.
    """
    rand_symbols = string.printable
    rand_text = ''.join(random.choice(rand_symbols) for i in range(random.randint(1000, 5000)))
    rand_text_bin = rand_text.encode('utf-8')
    with open('some_text.bin', 'wb') as file:
        file.write(rand_text_bin)


def reading_bin_file():
    """Counts symbols, words and lines in binary file.
    Opens some_text.bin file line by line then
    decodes it and counts symbols, words, lines from file."""
    with open('some_text.bin', 'rb') as file:
        symbols = 0
        words = 0
        lines = 0
        for line in file:
            text_line = line.decode('utf-8')
            symbols += len(text_line)
            words += len(text_line.split())
            lines += 1

    print(f'Symbols: {symbols}')
    print(f'Words: {words}')
    print(f'Lines: {lines}')


if __name__ == '__main__':
    generate_random_text()
    reading_bin_file()
