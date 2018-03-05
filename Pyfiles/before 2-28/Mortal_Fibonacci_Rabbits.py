def count_rabbit(n,m):
    num = [0 for x in range(0,n*m)]
    num[0] = 1
    count = 0
    for x in range(1,n):
        count = 0
        for y in range(1,m):
            num[m*x+y]=num[m*(x-1)+(y-1)]
            count+=num[m*(x-1)+y]
        num[m*x]=count
    count = 0
    for x in range(0,m):
        count+=num[(n-1)*m+x]
    return count

n = int(input('please enter the number of month after: '))
m = int(input('please enter the number of month that rabbit can live: '))

print(count_rabbit(n,m))
