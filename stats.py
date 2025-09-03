def get_book_text(filepath):
    return filepath.read()

def word_count(filepath):
    words = get_book_text(filepath).split()
    return len(words)

def char_count(filepath):
    chars = {}
    text = get_book_text(filepath)
    for char in text:
        char = char.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def report_count(chars):
    sorting = []
    for char in chars:
        sorting.append({"char" : char, "num" : chars[char]})
    def count(dict):
        return dict["num"]
    sorting.sort(reverse=True, key=count)
    return sorting