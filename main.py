with open("books/frankenstein.txt") as f:
    
    def first(n):
        return n[0]
    
    def second(n):
        return n[1]

    book = f.read()
    #title = f.name()
    print(f"--- Begin report of x ---")
    #lowercase = book.lower()
    #print(book.lower())
    letdic = dict()
    # this prints all the letters in the book on their own lines
    for i in book.lower():
        if i in letdic:
            letdic[i] += 1
        else:
            letdic[i] = 1
    thislist = letdic.items()
    sortlist = sorted(thislist, key = second, reverse = True)

    for i in sortlist:
        if first(i).isalpha() == False
            sortlist.pop(i)
    
    print(sortlist)
        
    
    
    #print(sortlist)
    
    
    #dickey = list(letdic.keys())
    #dicval = list(letdic.values())
    #counts = []
    
    
    #dickey.sort()
    #print(dickey)
    #print(sorted(dicval))
