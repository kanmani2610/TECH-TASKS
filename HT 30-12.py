 name = input('Enter a string: ')
alphabetic_characters = 0
numeric_characters = 0
special_characters = 0

def check(name):
    for char in name:
        if char.isalpha():  
            alphabetic_characters += 1
        elif char.isdigit():  
            numeric_characters += 1
        else:  
            special_characters += 1

    print(alphabetic_characters)
    print(numeric_characters)
    print(special_characters)

check(name)

            
    