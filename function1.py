number=int(input("Enter a number: "))

def checkNumber(number):
    if number>0 :
        print("Your Number is Positive")
    elif number<0:
        print("Your Number is Negative")
    else:
        print("You have entered 0")
        
checkNumber(number)