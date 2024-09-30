import sys

print(sys.argv)
mode = 'rb'
    
def get_filename():
    while True:
        fn = sys.argv[1] #input("Please enter filename: ")
        #if 
        try:
            f = open(fn, mode)
            f.close()
            return fn
        except FileNotFoundError:
            continue
    return None

filename = get_filename()
bytes = 0
line = []
with open(filename, mode) as file:
    fileContents = file.read()
for b in fileContents:
    bytes +=  1
    line.append(b)
    print("{0:0{1}x}".format(b,2), end=" ")
    if bytes%16 == 0:
        print("#", end="")
        for b2 in line:
            if (b2 >= 32) and (b2 <= 126):
                print(chr(b2), end="")
            else:
                print("*", end="")
        line = []
        print("")
        input()

print(" " * ((3*(16-len(line)))-1), "#", end="")
for b2 in line:
    if (b2 >= 32) and (b2 <= 126):
        print(chr(b2), end="")
    else:
        print("*", end="")
input()
