#!usr/python/env python3

def compute_stand_DNA(seq):
    result = ''
    for index in range(1,len(seq)+1):
        if seq[-index] == 'A':
            result+='T'
        elif seq[-index] == 'T':
            result+='A'
        elif seq[-index] == 'C':
            result+='G'
        elif seq[-index] == 'G':
            result+='C'
    return result

if __name__ == '__main__':
    
    print(compute_stand_DNA(input("enter a DNA sequence:\n")))