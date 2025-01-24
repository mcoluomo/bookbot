def main():

    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    dict_of_chars = count_of_chars(file_contents)
    dict_sort_chars = sort_on(dict_of_chars)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for char in dict_sort_chars:
        count = dict_sort_chars[char]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

def count_words(file_contents):
    file_contents = file_contents.split()
    count = 0
    for word in file_contents:
        count += 1
    return count

def count_of_chars(file_contents):
    num_of_chars = {}
    for char in file_contents.lower():
        if char in "abcdefghijklmnopqrstuvwxyz" and char not in num_of_chars:
            num_of_chars[char] = 1
        elif char in "abcdefghijklmnopqrstuvwxyz" and char  in num_of_chars:
            num_of_chars[char] += 1
    return num_of_chars

def sort_on(dict):
    myKeys = list(dict.keys())
    myKeys.sort()

    return {i: dict[i] for i in myKeys}

main()