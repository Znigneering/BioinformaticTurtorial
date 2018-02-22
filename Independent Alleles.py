def count(k,n):
    AABB = 0
    AABb = 0
    AAbb = 0
    AaBB = 0
    AaBb = 1
    Aabb = 0
    aaBB = 0
    aaBb = 0
    aabb = 0
    
    for x in range(0,k):
        AABB = AABB*(1/4)+AABb*(1/8)+AaBB*(1/4)+AaBb*(1/16)
        AABb = AABB*(1/4)+AABb*(1/4)+AAbb*(1/4)+AaBB*(1/8)+AaBb*(1/8)+Aabb*(1/8)
        AAbb = AABb*(1/8)+AAbb*(1/4)+AaBb*(1/16)+Aabb*(1/8)
        AaBB = AABB*(1/4)+AABb*(1/8)+AaBB*(1/4)+AaBb*(1/8)+aaBB*(1/4)+aaBb*(1/8)
        AaBb = AABB*(1/4)+AABb*(
    return Aa
    
k = input('please enter the number of generation:')
n = input('please enter the expect number of heterozygote:')

print(count(int(k),int(n)))
