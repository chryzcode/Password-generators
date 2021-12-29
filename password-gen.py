import random

s_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


lc_letters =  int(input('Enter the number of lower-case letters you need: '))
hc_letters =  int(input('Enter the number of higher-case letters you need: '))
nr_numbers = int(input('Enter the number of numbers you need: '))
nr_symbols = int(input('Enter the number of symbols you need: '))

# Easy

#password = ''

#for char in range(lc_letters):
    #password += random.choice(s_letters)

#for char in range(hc_letters):
    #password += random.choice(c_letters)

#for char in range(nr_numbers):
    #password += random.choice(numbers)

#for char in range(nr_symbols):
    #password += random.choice(symbols)

#print(password)

password_list = []

for char in range(lc_letters):
    password_list.append(random.choice(s_letters))

for char in range(hc_letters):
    password_list += random.choice(c_letters)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

for char in range(nr_symbols):
    password_list += random.choice(symbols)


random.shuffle(password_list)

password = ''
for char in password_list:
    password += char

print(password)
