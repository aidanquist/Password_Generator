#Password Generator
import keyboard
import termcolor
import colorama
import random
import string

print ('Generating a password:')

def ask_input(question):
    answered_wrong = True
    while answered_wrong == True:
        are_symbols = input(question)
        if are_symbols == 'Y':
            answered_wrong = False
            return True
        elif are_symbols == 'N':
            answered_wrong = False
            return False

#Get user input for password length
length = int(input('Password length: '))

#Get the user input for if symbols, numbers, and uppercase letters should be included
symbols = '' 
if ask_input('Include symbols? Enter Y or N: ') == True:
    symbols = string.punctuation
    print('Symbols included')

num = '' 
if ask_input('Include numbers? Enter Y or N: ') == True:
    num = string.digits
    print('Numbers included')

upper = '' 
if ask_input('Include uppercase letters? Enter Y or N: ') == True:
    upper = string.ascii_uppercase
    print('Uppercase letters included')


lower = string.ascii_lowercase

#Combine all selected characters
all = lower + upper + num + symbols
password = ''

#Randomly choose a character from the selected ones and add it to the password
for i in range(length):
    password = password + random.choice(all)


colorama.init()
temp = termcolor.colored(password, 'green')
print('Password: ' + temp)



