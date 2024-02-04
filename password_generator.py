import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_inp= int(input("How many letters would you like in your password?\n")) 
symbols_inp = int(input(f"How many symbols would you like?\n"))
numbers_inp = int(input(f"How many numbers would you like?\n"))

# password = ""
# for characters in range(1, letters_inp + 1):
#    letter_characters = random.choice(letters)
#    password += letter_characters
# print(password)


# password = ""
# for characters in range(1, letters_inp + 1):
#     password+= random.choice(letters)

# for characters in range(0, numbers_inp + 1):
#     password += random.choice(numbers)
    
# for characters in range(0, symbols_inp + 1):
#     password += random.choice(symbols)
    
# print(password)

password_list = []
for characters in range(1, letters_inp + 1):
    password_list.append(random.choice(letters))

for characters in range(0, numbers_inp + 1):
    password_list.append(random.choice(numbers))
    
for characters in range(0, symbols_inp + 1):
    password_list.append(random.choice(symbols))
    
# print(password_list)
# random.shuffle(password_list)
# print(password_list)

final_password = ""
for characters in password_list:
    final_password += characters
print(f"Your password is {final_password}")

