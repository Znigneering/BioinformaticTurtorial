#!usr/python/env python3


def enumeration(li,start,end):
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
    