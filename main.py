def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    # print(type(file_contents))

    wc = word_count(file_contents)
    # print(wc)

    cc = char_count(file_contents)
    # print(cc)

    """
    Only print counts for the characters that are in the alphabet

    --- Begin report of books/frankenstein.txt ---
    77986 words found in the document

    The 'k' character was found 1755 times


    --- End report ---
    """
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")

    for char in cc.keys():
        if char.isalpha():
            print(f"The '{char}' character was found {cc[char]} times")

    print("--- End report ---")


def word_count(file_contents):
    word_list = file_contents.split()
    # print(type(word_list))
    # print(word_list)

    return len(word_list)

def char_count(file_contents):
    char_count_dict = {}
    count = 0

    for char in file_contents.lower():
        if char not in char_count_dict.keys():
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
        count = 0

    # print(char_count_dict)
    return char_count_dict


main()