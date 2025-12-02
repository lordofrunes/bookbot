def main():

    from stats import get_num_words
    from stats import get_characters
    
    

    print("============ BOOKBOT ============")
    print("Analyzing frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("-------- Character Count -------")

    chars = get_characters()
    for entry in chars:
        ch = entry["char"]
        cnt = entry["count"]
        if ch.isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")

main()
