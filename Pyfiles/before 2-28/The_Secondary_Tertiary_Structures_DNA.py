kb = input('please enter a DNA sequence:')
count = len(kb)

for x in kb:
    if x == 'A':
        kb = kb[:count-1]+'T'+kb[count:]
    elif x == 'C':
        kb = kb[:count-1]+'G'+kb[count:]
    elif x == 'T':
        kb = kb[:count-1]+'A'+kb[count:]
    else:
        kb = kb[:count-1]+'C'+kb[count:]
    count -=1
print(kb)
