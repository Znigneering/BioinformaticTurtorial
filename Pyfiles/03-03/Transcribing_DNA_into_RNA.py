def DNA_into_RNA(seq):
    count = 0    
    for x in seq:
        if x == 'T':
            seq = seq[:count]+'U'+seq[count+1:]
        count+=1
    return seq

if __name__ == '__main__':

    seq = input('Please give a DNA sequence:')
    print(DNA_into_RNA(seq))