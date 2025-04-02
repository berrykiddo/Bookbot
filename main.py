import sys

from stats import get_num_words
from stats import count_characters
from stats import sort_on
from stats import create_sort_list_from_dict

def read_file(file_path): 
    with open(file_path) as f: 
        content = f.read()
    return content

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # text = read_file("books/frankenstein.txt")
    # print(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    words_сount = get_num_words(sys.argv[1])
    print(f"Found {words_сount} total words") 
    print("--------- Character Count -------")
    characters_count = count_characters(sys.argv[1])
    characters_sorted = create_sort_list_from_dict(characters_count)
    for char in characters_sorted: 
        character = char["character"]
        count = char["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")




main()
