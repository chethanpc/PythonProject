# Read a File and Handle Errors

try:
    file = open('sample.txt','r')
    first_line = file.readline().strip()
    second_line = file.readline()
    print('Reading file content:','\nLine 1:',first_line,'\nLine 2:',second_line)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
