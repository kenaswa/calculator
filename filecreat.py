file_name = input("Enter Your File Name: ")
content = input("Type your content: ")
with open(file_name, "w") as file:
    
      file.write(content)
#file = open("filetest2.txt", "r")
print(content)

#with open(file_name, "w") as file:
     #   file.write(content)
#f = open(file_name, "r")
#print(f.read())
#print(f"My File Name is {file_name} and my content is: {content}.")
#print(f.read())
#file.close()
