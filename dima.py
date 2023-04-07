old = int(input())
number = input()
new = int(input())
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

decimal = 0
for i in range(len(number)):
    decimal += alphabet.index(number[len(number) - 1 - i]) * (old ** i)

new_number = []
while decimal > 0:
    new_number.append(decimal % new)
    decimal = int(decimal / new)
    
for i in new_number[::-1]:
    print(alphabet[i], end='')
