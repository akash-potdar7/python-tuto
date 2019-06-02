import runner_up

n = runner_up.calc_runner_up_score([3,12,5,7,11])
print('runner up score', n)

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# find students with second lowest score
# first extract second min score
score = runner_up.find_second_lowest_score(students)
print('second lowest score', score)

# from second min score, lookup for student with that score
students = runner_up.find_students_with_score(students, score)
print('student who scored second lowers', students)
