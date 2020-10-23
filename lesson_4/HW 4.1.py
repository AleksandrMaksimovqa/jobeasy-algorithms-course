def longer_word(string):
    l_word = ""
    for word in string.split():
        if len(word) > len(l_word):
            l_word = word
    return l_word


print(longer_word('55555 1 22 333 4444 55555 333 qqqqq'))