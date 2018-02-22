def expect_dominant_phenotype(g1,g2,g3,g4,g5,g6):
    return 2*g1+2*g2+2*g3+1.5*g4+g5

gtype1 = int(input('please enter the number of AA-AA: '))
gtype2 = int(input('please enter the number of AA-Aa: '))
gtype3 = int(input('please enter the number of AA-aa: '))
gtype4 = int(input('please enter the number of Aa-Aa: '))
gtype5 = int(input('please enter the number of Aa-aa: '))
gtype6 = int(input('please enter the number of aa-aa: '))

print(str(expect_dominant_phenotype(gtype1,gtype2,gtype3,gtype4,gtype5,gtype6)))
