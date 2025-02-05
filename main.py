
def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = num_of_words(text)
    print(f"{num_words} words found in the document")
    characters_count = num_of_characters(text)
    print(characters_count)

def num_of_words(text):
    words = text.split()
    return len(words)

def num_of_characters(text):
    lowered_text = text.lower()
    characters_dict = {}
    for character in lowered_text:
        if character in characters_dict:
            characters_dict[character] += 1
        else: 
            characters_dict[character] = 1
    return characters_dict

      

def book_text(path):
    with open(path) as f:
        return f.read()
    
  


if __name__ == "__main__":
    main()