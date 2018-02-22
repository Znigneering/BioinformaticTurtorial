def indexOf(s,t):
    x = len(s)
    y = len(t)
    if x>=y:
        count = 0
        while count<x-y:
            if s[count:count+y] == t:
                print(count+1,end=' ')
            count+=1

s = input('please enter the first DNA squence s: ')
t = input('please enter the second DNA squence t: ')

indexOf(s,t)
