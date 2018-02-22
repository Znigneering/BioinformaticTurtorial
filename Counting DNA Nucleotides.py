A = 0
T = 0
G = 0
C = 0

kb = input('Please give a DNA sequence:')

for x in kb:
    if x == 'A':
        A+=1
    elif x == 'T':
        T+=1
    elif x == 'C':
        C+=1
    else:
        G+=1 
print('A: '+str(A)+' T: '+str(T)+' C: '+str(C)+' G: '+str(G))
