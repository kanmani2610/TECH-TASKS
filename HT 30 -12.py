name = input('Enter a string: ')
def validate_string(name):
    alphabet = 0 
    special_char = 0  
    for char in name:
        if char.isalpha(): 
            alphabet = 1
        elif not char.isalnum():
            special_char = 1
    if alphabet and special_char:
        print("it contains both")
    else:
        print("no")
result=validate_string(name)
print(result)

