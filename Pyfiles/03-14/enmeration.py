#!usr/python/env python3

def enumeration(li,start,end):
    """
        Its going to permutating all the list elements.
        
        Arguments:
            li --- Type: list | Description: the list contains all the elements
            start --- Type: int | Description: the start index of the permutation
            end --- Type: int | Description: the end index of the permutation
        Retured:
            seq --- Type: global string | Description: the set of all permutations
            count --- Type: global int | Description: the number of permutations
    """
    for x in range(start,end):
        global count
        global seq
        enumeration(li,start+1,end)
        li.append(li.pop(start))
        if (start == end-1):
            count += 1
            for i in li:
                seq+=str(i)+' '
            seq+='\n'
            

if __name__ == "__main__":
    count = 0
    seq = ""
    length = int(input("enter a number:"))
    li = [ i for i in range(1,length+1)]
    enumeration(li,0,length)
    print(count)
    print(seq)
    