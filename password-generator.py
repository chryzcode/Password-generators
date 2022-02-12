import random
print('\nI can assist you in generating a password!')

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

number = int(input('\nInput the number of password you need: '))


length = int(input('Input the length of your proposed password: '))

print('\nHere are your proposed password: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print(passwords)
