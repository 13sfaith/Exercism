def is_isogram(string):
    lets = []
    string = string.upper()

    for j in string:
        if j in lets and j.isalpha():
            return False
        else:
            lets.append(j)

    return True
