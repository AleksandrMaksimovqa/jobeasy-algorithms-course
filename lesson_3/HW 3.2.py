

def replace_substr(string, old_sub_str, new_sub_str):
    for i in range(len(string)-len(old_sub_str)):
        if string[i:i+len(old_sub_str)] == old_sub_str:
            string[i:i + len(old_sub_str)] = new_sub_str
    return "".join(string)


string = list(input('Enter a string: ', ))

substring  = list(input('What substring you want to replace: ', ))

new_substring = list(input('Enter a new substring: ', ))

print(replace_substr(string,substring,new_substring))