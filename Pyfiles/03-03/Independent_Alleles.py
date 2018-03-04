global num

def count(k,n):
    
    import math
    
    num = pow(2,k) # num of children in k-th generation
    
    if n == 0:
        return 0
    else:
        binomial = math.factorial(num)/(math.factorial(n-1)*math.factorial(num-n+1))*math.pow(1/4,n-1)*math.pow(3/4,num-n+1)
        return count(k,n-1)+binomial

if __name__ == "__main__":
    
    k = input('please enter the number of generation:')
    n = input('please enter the expect number of heterozygote:')
    print(1-count(int(k),int(n)))
