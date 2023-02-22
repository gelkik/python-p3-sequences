#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        array = [0,1]
        i=0
        while len(array)<12:
            num = array[i]+array[i+1]
            array.append(num)
            i+=1
        print(array[0:length])

