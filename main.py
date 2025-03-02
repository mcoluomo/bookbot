from stats import count_words, sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():

    with open(sys.argv[1]) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    dict_of_chars = count_of_chars(file_contents)
    dict_sort_chars = sort_on(dict_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in dict_sort_chars:
        count = dict_sort_chars[char]
        print(f"{char}: {count}")

    print("============= END ===============")

def count_of_chars(file_contents):
    num_of_chars = {}
    for char in file_contents.lower():
        if char in "abcdefghijklmnopqrstuvwxyz" and char not in num_of_chars:
            num_of_chars[char] = 1
        elif char in "abcdefghijklmnopqrstuvwxyz" and char  in num_of_chars:
            num_of_chars[char] += 1
    return num_of_chars

main()