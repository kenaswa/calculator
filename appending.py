f = open("fruits.txt", "a")
f.write(" Berrys and Oranges")
f.close()

#open and read the file after the appending:
f = open("fruits.txt", "r")
print(f.read())