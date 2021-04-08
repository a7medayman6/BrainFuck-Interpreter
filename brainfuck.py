import sys
import os.path
import re
import getch

def initArray(size):
    arr = []
    for _ in range(size):
        arr.append(0)
    
    return arr

def read(path):
    file = ""

    if os.path.isfile(path):
        f = open(path, "r")
        file = f.read()
        f.close()
    else :
        print("Error Opening The File.")

    return file

def cleanUp(code):
    return ''.join(filter(lambda letter: letter in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

def incPtr(ptr, limit):
    if ptr == limit:
        ptr = 0
    else:
        ptr += 1
    return ptr

def decPtr(ptr, limit):
    if ptr == 0:
        ptr = limit - 1
    else:
        ptr -= 1
    return ptr

def map_brackets(code):
    stack = []
    dictionary = {}

    for i in range(len(code)):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            if len(stack) == 0:
                print("Error: closed barcket [ with no opening bracket ]")
                exit
            s = stack.pop()
            dictionary[s] = i
            dictionary[i] = s
    if len(stack) > 0:
        print("Error: opend bracket [ with no closing bracket ]")
        exit
    return dictionary


def interpret(code, limit):
    ptr = 0
    array = initArray(limit)
    bracketsMap = map_brackets(code)
    i = 0
    while i < len(code):
        command = code[i]

        if command == '>':
            ptr = incPtr(ptr, limit)

        elif command == '<':
            ptr = decPtr(ptr, limit)

        elif command == '+':
            if array[ptr] < 255:
                array[ptr] += 1
            else :
                array[ptr] = 0

        elif command == '-':
            if array[ptr] > 0:
                array[ptr] -= 1
            else :
                array[ptr] = 255

        elif command == '.':
            sys.stdout.write(chr(array[ptr]))

        elif command == ',':
            array[ptr] = ord(getch.getch())
            sys.stdout.write(chr(array[ptr]))

        elif command == '[':
            #print("open : \t", bracketsMap[i])
            if array[ptr] == 0:
                i = bracketsMap[i] - 1
        elif command == ']':
            if array[ptr] != 0:
            #    print("close : \t", bracketsMap[i])
                i = bracketsMap[i] - 1

        i += 1

def main():
    size = 30000
    file = read(sys.argv[1])
    code = cleanUp(file)
    interpret(code, size)
    print()

if __name__ == "__main__": main()