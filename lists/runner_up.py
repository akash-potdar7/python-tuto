def calc_runner_up_score(score_list):
    return second_max(score_list)

def calc_second_lowest_score(score_list):
    return second_min(score_list)

def second_max(list):
    maxie = find_max(list)
    sec_max = find_min(list)
    for x in list:
        if x > maxie:
            sec_max = maxie
            maxie = x
        elif x > sec_max and x < maxie:
            sec_max = x
    return sec_max

def second_min(list):
    minie = find_max(list)
    sec_min = find_min(list)
    for x in list:
        if x < minie:
            sec_min = minie
            minie = x
        elif x < sec_min and x > minie:
            sec_min = x
    return sec_min

def find_max(list):
    maxie = list[0]
    for i in list:
        if i > maxie:
            maxie = i
    return maxie

def find_min(list):
    minie = list[0]
    for i in list:
        if i < minie:
            minie = i
    return minie

def find_second_lowest_score(students):
    scores = extract_score(students, 1)
    return second_min(scores)

def extract_score(students_score_list, pos):
    scores = []
    for s in students_score_list:
        scores.append(s[pos])
    return scores

def extract_element_from_list(list, score, pos):
    mapped_items = []
    for s in list:
        if (s[pos] == score):
            mapped_items.append(s)
    return mapped_items

def find_students_with_score(student, score):
    return extract_element_from_list(student, score, 1)
