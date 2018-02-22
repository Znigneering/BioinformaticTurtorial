count = 0

kb = input('Please give a DNA sequence:')

for x in kb:
    if x == 'T':
        kb = kb[:count]+'U'+kb[count+1:]
    count+=1
print(kb)

