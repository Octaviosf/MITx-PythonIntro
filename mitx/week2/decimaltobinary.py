dec = int(input('Input decimal to convert to binary: '))
bit = ''
num = dec
while num > 0:
    bit = str(num%2) + bit
    num = num//2

if dec == '0':
    bit = '0'

print('The decimal', dec, 'has a binary representation of', bit + '.')
print('Using the builtin function bin(decimal), the binary representation of',dec,'is',str(bin(dec)))

