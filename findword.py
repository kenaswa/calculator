#def print_line_with_word(file_path, word):
def print_line_with_word(fruit.txt, Mangos): 
    with open(fruit.txt, 'r') as file: 
        for line in file: 
            if Mangos in line: 
                print(line) 
 
#file_path = 'path/to/file.txt' 
#word = 'example' 
print_line_with_word(file_path, word) 