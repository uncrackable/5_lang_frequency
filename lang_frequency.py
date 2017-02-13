import re
import os
import argparse
from collections import Counter
MOST_COMMON_WORDS = 10


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read().lower()


def get_most_frequent_words(text):
    result = re.findall(r'\w+', text)
    return Counter(result).most_common(MOST_COMMON_WORDS)


def pretty_print(words):
    for idx, item in enumerate(words):
        print('{}. {} : {}'.format(idx+1, item[0], item[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
                                     "This script displays in console "
                                     "ten most popular words in text file")
    parser.add_argument('-f', '--file', required='True',
                        help='filepath to your text file')
    args = parser.parse_args()
    data = load_data(args.file)
    if data is None:
        print('File or folder with that name does not exist')
    else:
        pretty_print(get_most_frequent_words(data))

