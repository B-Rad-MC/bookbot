from stats import word_count, char_count, report_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    with open(filename) as f:
        print("----------- Word Count ----------")
        print(f"Found {word_count(f)} total words")
        f.seek(0)
        print("--------- Character Count -------")
        char_list = report_count(char_count(f))
        for char in char_list:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()