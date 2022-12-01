def split(inputstring):
    return ' '.join([i.lower() for i in inputstring])

def combine(inputstring):
    inputstring.replace(" ", "")
    return inputstring


def remove_spaces_and_capitalize(s):
    return ''.join(c.upper() if i > 0 and s[i-1] == ' ' else c for i, c in enumerate(s))

def convert_to_lowercase(string):
    return string.lower()

def add_spaces_before_uppercase(string):
    result = ""
    for i in range(len(string)):
        if i != 0 and string[i].isupper():
            result += " "
        result += string[i]
    return result
if __name__ == '__main__':
    string = input("Enter a string: ")
    #string = add_spaces_before_uppercase(string)
    #string = convert_to_lowercase(string)
    string = remove_spaces_and_capitalize(string)
    print(string)

