from stats import wordcount, get_book_text, charactercount
import sys



def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the file path as a command-line arguement.")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        book_content = get_book_text(file_path)
        if isinstance(book_content, str) and not book_content.startswith("Error"):
            word_count = wordcount(book_content)  # Call wordcount and store the result
            char_counts = charactercount(book_content)
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {file_path}")
            print("----------- Word Count ----------")
            print(f"'Found {word_count} total words'")
            print("--------- Character Count -------")
            for char, count in char_counts.items():
                if char.isalpha():
                    print(f"'{char}: {count}'")
            print("============= END ===============")
        else:
            print("Could not process word count due to an error in reading the file.")

if __name__ == "__main__":
    main()