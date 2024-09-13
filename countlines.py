#with open("fruits.txt", 'r') as file:
file=open("fruits.txt", 'r')
lines = len(file.readlines())
print('Total Number of lines:', lines)