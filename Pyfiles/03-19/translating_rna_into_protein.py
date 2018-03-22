def mRNA_into_protein(seq):
    x = len(seq)
    count = 0
    protein = ''
    
    while count < x:
        if seq[count:count+3]=='UUU' or seq[count:count+3]=='UUC':
            protein+='F'
        elif seq[count:count+3]=='UUA' or seq[count:count+3]=='UUG' or seq[count:count+3]=='CUU' or seq[count:count+3]=='CUC' or seq[count:count+3]=='CUA' or seq[count:count+3]=='CUG':
            protein+='L'
        elif seq[count:count+3]=='UCU' or seq[count:count+3]=='UCC' or seq[count:count+3]=='UCA' or seq[count:count+3]=='UCG':
            protein+='S'
        elif seq[count:count+3]=='UAU' or seq[count:count+3]=='UAC':
            protein+='Y'
        elif seq[count:count+3]=='UGU' or seq[count:count+3]=='UGC':
            protein+='C'
        elif seq[count:count+3]=='UGG':
            protein+='W'
        elif seq[count:count+3]=='CCU' or seq[count:count+3]=='CCC' or seq[count:count+3]=='CCA' or seq[count:count+3]=='CCG':
            protein+='P'
        elif seq[count:count+3]=='CAU' or seq[count:count+3]=='CAC':
            protein+='H'
        elif seq[count:count+3]=='CAA' or seq[count:count+3]=='CAG':
            protein+='Q'
        elif seq[count:count+3]=='CGU' or seq[count:count+3]=='CGC' or seq[count:count+3]=='CGA' or seq[count:count+3]=='CGG':
            protein+='R'
        elif seq[count:count+3]=='AUU' or seq[count:count+3]=='AUC' or seq[count:count+3]=='AUA':
            protein+='I'
        elif seq[count:count+3]=='AUG':
            protein+='M'
        elif seq[count:count+3]=='ACU' or seq[count:count+3]=='ACC' or seq[count:count+3]=='ACA' or seq[count:count+3]=='ACG':
            protein+='T'
        elif seq[count:count+3]=='AAU' or seq[count:count+3]=='AAC':
            protein+='N'
        elif seq[count:count+3]=='AAA' or seq[count:count+3]=='AAG':
            protein+='K'
        elif seq[count:count+3]=='AGU' or seq[count:count+3]=='AGC':
            protein+='S'
        elif seq[count:count+3]=='AGA' or seq[count:count+3]=='AGG':
            protein+='R'
        elif seq[count:count+3]=='GUU' or seq[count:count+3]=='GUC' or seq[count:count+3]=='GUA' or seq[count:count+3]=='GUG':
            protein+='V'
        elif seq[count:count+3]=='GCU' or seq[count:count+3]=='GCC' or seq[count:count+3]=='GCA' or seq[count:count+3]=='GCG':
            protein+='A'
        elif seq[count:count+3]=='GAU' or seq[count:count+3]=='GAC':
            protein+='D'
        elif seq[count:count+3]=='GAA' or seq[count:count+3]=='GAG':
            protein+='E'
        elif seq[count:count+3]=='GGU' or seq[count:count+3]=='GGC' or seq[count:count+3]=='GGA' or seq[count:count+3]=='GGG':
            protein+='G'
        else:
            break
        count+=3
        
    return protein

if __name__ == "__main__":
    
    seq = input('enter a mRNA sequence: ')
    
    print(mRNA_into_protein(seq)[0])
