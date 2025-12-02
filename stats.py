def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def get_num_words():

    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    num_words = len(words)
    return num_words

def sort_on(items):
    return items["count"]

def get_characters():

    
    text = get_book_text("books/frankenstein.txt")
    Lower_text = text.lower()
    characters = {}

    for t in Lower_text:
        if t in characters:
            characters[t] += 1
        else:
            characters[t] = 1

  #I now need to have a list of dict with key "char" for each character and a key "count" for each count
    char_list = []

    for ky in characters:
        char_list.append({"char": ky, "count": characters[ky]})

    char_list.sort(key=sort_on, reverse=True)

    return char_list

    

    

get_num_words()
get_characters()



