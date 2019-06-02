def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if isDivisibleBy(num, i):
                print(num, 'is not a prime number')
                break
            else:
                print(num, 'is a prime number')
                break
    else:
        print(str(num) + ' is not a prime number yo')

def isDivisibleBy(num, i):
    isDivisble = False
    if (num % i) == 0:
        isDivisble = not isDivisble
    return isDivisble

isPrime(7)
