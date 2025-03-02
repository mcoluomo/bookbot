def count_words(file_contents):
    file_contents = file_contents.split()
    count = 0
    for word in file_contents:
        count += 1
    return count

def sort_on(dict):
    myKeys = list(dict.keys())
    myKeys.sort()

    return {i: dict[i] for i in myKeys}