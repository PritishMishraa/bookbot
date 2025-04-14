import sys
from stats import get_book_text, count_character_frequency, sort_character_frequency

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}...")
    num_words = len(book_text.split())
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count --------")
    character_counts = count_character_frequency(book_text)
    sorted_character_counts = sort_character_frequency(character_counts)
    for character in sorted_character_counts:
        print(f"{character['character']}: {character['count']}")

if __name__ == "__main__":
    main()