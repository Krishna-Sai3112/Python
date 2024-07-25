def words_to(file_name,words_to_find):
    try:
        with open(file_name,"r") as file:
            content=file.read()
            found_words=[]
            for word in words_to_find:
                if word in content:
                    found_words.append(word)
            return found_words
    except FileNotFoundError:
        print("File not found")
def main():
    file_name=input("Enter file name:")
    words_to_find=input("Enter words to find: ").split()
    words_to_find=[word.strip() for word in words_to_find]
    found_Words=words_to(file_name,words_to_find)
    if found_Words:
        for word in found_Words:
            print(word)
    else:
        print("Not found")
main()