activefile = "books/frankenstein.txt"

with open(activefile) as f:
    
    def first(n):
        return n[0]
    
    def second(n):
        return n[1]

    book = f.read()
    letdic = dict()
    print(f"--- Begin report of {activefile} ---")
    
    # this counts all the symbols in the book and outputs as a dict
    for i in book.lower():
        if i in letdic:
            letdic[i] += 1
        else:
            letdic[i] = 1

    # translate the dictionary into a tuple, then use the second key to sort        
    thislist = letdic.items()
    sortlist = sorted(thislist, key = second, reverse = True)
    #print(sortlist[1])

    for i, k in enumerate(sortlist):
        if first(k).isalpha() == True:
            print(f"The '{first(k)}' character was found {second(k)} times")
                  
    print("--- End Report ---")
