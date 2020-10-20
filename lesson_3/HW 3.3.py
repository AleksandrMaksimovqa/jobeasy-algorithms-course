
string1 = input(f"Enter a string: ")

def str_decompress(string):
    number = ['1','2','3','4','5','6','7','8','9','0']
    result = ""
    amount = ""
    for i in range(len(string)-1):
        if string[i] not in number:
            result += "".join(string[i])
            litter = string[i]
        else:
            amount += "".join(string[i])
            if string[i+1] not in number:
                result += "".join(litter * (int(amount)-1))
                amount = ""
    if string[-1] in number:
        amount += "".join(string[-1])
        result += "".join(litter * (int(amount) - 1))
    else:
        result += "".join(string[-1])
    return result

print(str_decompress(string1))