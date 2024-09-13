content = input("List of Fruits: ")
with open("fruits.txt", "w") as file:
    
      file.write(content)
file = open("fruits.txt", "r")
print(file.read())
file.close()