import shutil 
  
# use copyfile()
with open("file6.txt", "w"):
    shutil.copyfile('fruits.txt','file6.txt')
    file = open("file6.txt", "r")
    print(file.read())