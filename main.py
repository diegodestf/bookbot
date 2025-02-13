def main():
    with open('./books/frankestein.txt') as f:
        file_contents = f.read()
    #print(file_contents)
    wordCount = getWordCount(file_contents)
    charCount = getCharCount(file_contents)
    print(f"--- Begin report of {f.name} ---")
    print(f"{wordCount} words found in the document\n")

    for char, count in sorted(charCount.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{char}' character was found {count} times")


def getWordCount(text):
    return len(text.split())

def getCharCount(text):
    count = {}

    for char in text.lower():
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    
    return count

main()