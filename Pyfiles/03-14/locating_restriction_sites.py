#!usr/pyhton/env pyhton3

def find_reverse_palindrome(seq):
    result = ''
    for x in range(0,len(seq)-1):
        pair = 0
        while is_reseverse(seq[x-pair],seq[x+1+pair]) and pair < 6:
            pair += 1
            if pair != 1:
                result += str(x+2-pair)+' '+str(pair*2)+' \n'
            if x-pair < 0 or x+1+pair >= len(seq):
                break
    return result

def is_reseverse(x,y):
    if x == 'C' and y == 'G':
        return True
    elif x == 'G' and y == 'C':
        return True
    elif x == 'A' and y == 'T':
        return True
    elif x == 'T' and y == 'A':
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(find_reverse_palindrome(input('enter the DNA seq:')))