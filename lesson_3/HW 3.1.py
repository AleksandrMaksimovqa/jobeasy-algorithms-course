def count_char(string, char):
    counter = 0
    for i in range(len(string)):
        if char in string:
            counter += 1
            string = string.replace(char, "",1)
    return counter


print(count_char('qwertyqqwe3rty', 'qw'))