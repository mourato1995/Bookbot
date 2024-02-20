

def main():
    book_path = "github.com/mourato1995/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    stringdic = get_num_letters(text)
    report = list_of_dics(stringdic)
    report.sort(key=sort_on,reverse=True)
    
    #stringlist = list(stringdic.values())
    #stringlist.sort(reverse=True,key=sort_on)
    #report = sort_on(stringlist)

    
    print(text)
    print(f"{num_words} words found in document")
    print(report)
    #print(stringdic)
    #print(report)
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read().lower()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    strings_dict = {}
    for letter in text:
        if letter.isalpha():
            if letter in strings_dict:
                strings_dict[letter] += 1
            else:
                strings_dict[letter] = 1
    return strings_dict

def list_of_dics(stringdic):
    list_of_dics = []
    for key,value in stringdic.items():
        list_of_dics.append({'letter': key, 'count': value})
    return list_of_dics

def sort_on(strings_dict):
    return strings_dict["count"]

main()

    