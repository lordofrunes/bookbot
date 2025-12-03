

def get_num_words(text):

    words = text.split()
    num_words = len(words)
    return num_words

def sort_on(items):
    return items["count"]

def get_characters(text):

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

    



