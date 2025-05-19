def get_book_text(file_path):
# Takes a filepath and returns a string containing the text of the file #
    try:
         with open(file_path, 'r') as f:
             file_contents = f.read()
             return file_contents
    except FileNotFoundError:
        return f"Error: file not found at '{file_path}'"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    file_path = '/home/greghill91/Projects/bookbot/books/frankenstein.txt' # Book file path
    book_string = get_book_text(file_path)
    return book_string 

def wordcount(book_string):
    try:
        split_string = book_string.split()
        count = len(split_string)
        return count   
    except Exception as e:
        return f"An error occurred: {e}"

from collections import Counter, OrderedDict 

def charactercount(book_string):
    try:
        lower_case = book_string.lower()
        charCount = Counter(lower_case) #Returns a Counter Object which is like a dictionary
        sortedCount = sorted(charCount.items(), key=lambda item: item[1], reverse=True)
        characters = OrderedDict(sortedCount)
        return characters
    except Exception as e:
        return f"An error occurred: {e}"
    

if __name__ == "__main__":
    book_content = main()
    if isinstance(book_content, str) and not book_content.startswith("Error"):
        wordcount(book_content)
    else:
        print("Could not process word count due to an error in reading the file.")
