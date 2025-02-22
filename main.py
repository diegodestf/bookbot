from stats import getWordCount
import sys

def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            file_contents = f.read()
    else:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    wordCount = getWordCount(file_contents)
    charCount = getCharCount(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f.name}")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")



    for char, count in sorted(charCount.items(), key=lambda x: x[1], reverse=True):
        print(f"{char}: {count}")




def getCharCount(text):
    count = {}

    for char in text.lower():
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    
    return count

main()