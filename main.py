import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    
    book_text = get_book_text(book_path)

    
    if "The file was not found." in book_text or "An error occurred" in book_text:
        print(book_text)
        sys.exit(1)

    print(f"Successfully loaded the book from {book_path}")
    print("============ BOOKBOT ============")
    print("Analyzing book found at:", book_path)

    
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f'Found {num_words} total words')

    
    print("--------- Character Count -------")
    sorted_char_counts = count_characters(book_text)

    print("Character counts (sorted):")
    for char, count in sorted_char_counts:
        print(f"{char}: {count}")

if __name__ == '__main__':
    main()
