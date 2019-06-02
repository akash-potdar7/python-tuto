print('starting...')
def sum(x, y, z=50):
    if isinstance(x, int) and isinstance(y, int):
        return x+y+z
    else:
        return 'Invalid args' + '->' + str(x) + ', ' + str(y)

# print(sum('Jon', 'Snow'))
# print(sum(10, 20))
# print(sum(y=10, x=20))
# print(sum(y=20, x=30))

def varadicFn(*x):
    sum=0
    for a in x:
        print(a)
        sum = sum + a
    return sum
    # print(a)
    # print(x)
    # print(isinstance(x, tuple))

print(varadicFn(1,2,3))