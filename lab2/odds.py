odds = []
evens = []
numbers = range(0,100)
for n in numbers:
    if n%2 != 0:
        odds.append(n)
    else:
        evens.append(n)
print('odd numbers', odds)
print('even numbers', evens)