def count_substring(string, sub_string):
    return string.count(sub_string)

def substring_occurances(string, sub_string):
    occ = 0
    sub_len = len(sub_string)
    s_len = len(string)

    for i in range(s_len):
        if string[i : i+sub_len] == sub_string:
            occ += 1
    return occ
