def sorter(e):
    return e['count']

def count_words(string):
    words = string.split()
    return len(words)

def count_char(string):
    string = string.lower()
    chars = {}
    dict_list = []

    for i in string:
        if i in chars:
            chars[i] = chars[i] + 1
        else:
            chars[i] = 1

    for key in chars:
        if key.isalpha():
            dict_list.append({"letter": key, "count": chars[key]})
    return dict_list


def main():
    with open("books/frankenstein.txt") as f:
        data = f.read()
        word_count = count_words(data)
        char_dict = count_char(data)
        
    char_dict.sort(reverse=True, key=sorter)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n")

    for key in range(len(char_dict)):
        print(f"The '{char_dict[key]['letter']}' character was found {char_dict[key]["count"]} times")
    print("--- End report ---")

main()