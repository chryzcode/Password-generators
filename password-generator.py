import random
print('\nI can assist you in generating a password!')

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

number = input('\nInput the number of password you need: ')
number = int(number)

length = input('Input the length of your proposed password: ')
length = int(length)

print('\nHere are your proposed password: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print(passwords)
