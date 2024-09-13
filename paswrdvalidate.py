password = input("Enter password: ")

number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
lowercaseletters = "abcdefghijklmnopqrstuvwxyz"
uppercaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

contains_numbers = False
contains_letters = False


"breanda"

for char in password:
     
    for num in number:
        "2" and  "2" 
        if char == num:
            contains_numbers = True
            break  

    
    for letter in lowercaseletters:
        if char == letter:
            contains_letters = True
            break  
    
    
    for letter in uppercaseletters:
        if char == letter:
            contains_letters = True
            break  

if len(password) < 8:
    print("Your password is too short")
elif  contains_numbers==False or  contains_letters ==False:
    print("Your password should contain both numbers and letters")
else:
    print("Password meets the criteria")
    