import sys
from stats import get_num_words
from stats import get_characters

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    
    num_words = get_num_words(text)
    chars = get_characters(text)
    

    print("============ BOOKBOT ============")
    print(f"Analyzing {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")

    
    for entry in chars:
        ch = entry["char"]
        cnt = entry["count"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")

main()
