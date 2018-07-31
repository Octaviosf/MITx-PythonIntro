#does 2**x return a value evenly divisible by 10?
x = 0
while 2**x%10 != 0:
    x += 1
    print(x)
    if x == 200000:
        break
if x == 200000:
    print('From 2^0 to 2^200000 there was no integer value evenly divisible by 10.')
else:
    print('2 to the power of',x, 'returns a value evenly divisible by 10: ', str(2**x))
