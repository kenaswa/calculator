#python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("numbers.txt", "w") as file:
# file = open("numbers.txt", "w")
#number.sort()
#for i in range(11):
    file.writelines(lines) #(stri(i) + "\n")
    for line in lines:
        print(line.strip())
    file.close()