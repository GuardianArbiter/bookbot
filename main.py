from stats import wordcount, get_book_text, charactercount

def main():
    file_path = '/home/greghill91/Projects/bookbot/books/frankenstein.txt'
    book_content = get_book_text(file_path)
    if isinstance(book_content, str) and not book_content.startswith("Error"):
        word_count = wordcount(book_content)  # Call wordcount and store the result
        print(f"'{word_count} words found in the document'")
        char_counts = charactercount(book_content)
        print(char_counts) 
    else:
        print("Could not process word count due to an error in reading the file.")

if __name__ == "__main__":
    main()