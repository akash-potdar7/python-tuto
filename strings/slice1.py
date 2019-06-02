def mutate_string_by_list_conversion(string, pos, char):
    l = list(string)
    l[pos] = char
    string = ''.join(l)
    return string

def mutate_string_by_slice(string, pos, char):
    string = string[:pos] + str(char) + string[pos+1:]
    return string
