
# open both files 
with open('fruits.txt','r') as firstfile, open('file1.txt','w') as secondfile: 
      
    # read content from first file 
    for line in firstfile: 
               
             # write 'w'/append 'a' content to second file 
             secondfile.write(line)
             file = open("file1.txt", "r")
             print(file.read())
             file.close()
             print("File reading ended")