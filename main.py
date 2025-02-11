
def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = num_of_words(text)
    characters_count = num_of_characters(text)
    report = report_generator(characters_count, num_words, book_path)
    print(report)

def book_text(path):
    with open(path) as f:
        return f.read()

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

def sort_on(dict):
    return dict["num"]


def report_generator(characters_count, num_words, book_path):
    characters_list = []
    for c in characters_count:
        if c.isalpha() == True:
            characters_list.append({"character": c, "num": characters_count[c]})
    characters_list.sort(reverse=True, key=sort_on)
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{num_words} words found in the document\n\n"
    for i in characters_list:
        report += f"The '{i["character"]}' character was found {i["num"]} times\n"
    report += f"\n --- End report ---"
    return report


if __name__ == "__main__":
    main()