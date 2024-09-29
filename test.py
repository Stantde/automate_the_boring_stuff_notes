'''
Write a simple text file then read the file in bytes.
'''
filemode = "w"
filename = "simple_text.txt"
with open(filename, filemode) as file:
    file.write("This is a test")
    filemode = "rb"

with open(filename, filemode) as file:
    line_count = 0
    n = 2
    x = file.read(n) #reads a single byte into the buffer
    while x:
        print(str(line_count),":\t", end='')
        print(x.hex(' '))
        x = file.read(n)
        line_count += 1

