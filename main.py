def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print("These are the letter counts:")
    lettercounts = get_num_letters(text)
    for letter, count in sorted(lettercounts.items()):
        print(f"char {letter} found {count} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    lowertext = text.lower()
    counts = {}
    for char in lowertext:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()