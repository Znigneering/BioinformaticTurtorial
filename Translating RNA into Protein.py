kb = input('enter a DNA sequence: ')

x = len(kb)
count = 0
protein = ''

print(x/3)

while count < x:
    print(count," ",kb[count:count+3])
    if kb[count:count+3]=='UUU' or kb[count:count+3]=='UUC':
        protein+='F'
    elif kb[count:count+3]=='UUA' or kb[count:count+3]=='UUG' or kb[count:count+3]=='CUU' or kb[count:count+3]=='CUC' or kb[count:count+3]=='CUA' or kb[count:count+3]=='CUG':
        protein+='L'
    elif kb[count:count+3]=='UCU' or kb[count:count+3]=='UCC' or kb[count:count+3]=='UCA' or kb[count:count+3]=='UCG':
        protein+='S'
    elif kb[count:count+3]=='UAU' or kb[count:count+3]=='UAC':
        protein+='Y'
    elif kb[count:count+3]=='UGU' or kb[count:count+3]=='UGC':
        protein+='C'
    elif kb[count:count+3]=='UGG':
        protein+='W'
    elif kb[count:count+3]=='CCU' or kb[count:count+3]=='CCC' or kb[count:count+3]=='CCA' or kb[count:count+3]=='CCG':
        protein+='P'
    elif kb[count:count+3]=='CAU' or kb[count:count+3]=='CAC':
        protein+='H'
    elif kb[count:count+3]=='CAA' or kb[count:count+3]=='CAG':
        protein+='Q'
    elif kb[count:count+3]=='CGU' or kb[count:count+3]=='CGC' or kb[count:count+3]=='CGA' or kb[count:count+3]=='CGG':
        protein+='R'
    elif kb[count:count+3]=='AUU' or kb[count:count+3]=='AUC' or kb[count:count+3]=='AUA':
        protein+='I'
    elif kb[count:count+3]=='AUG':
        protein+='M'
    elif kb[count:count+3]=='ACU' or kb[count:count+3]=='ACC' or kb[count:count+3]=='ACA' or kb[count:count+3]=='ACG':
        protein+='T'
    elif kb[count:count+3]=='AAU' or kb[count:count+3]=='AAC':
        protein+='N'
    elif kb[count:count+3]=='AAA' or kb[count:count+3]=='AAG':
        protein+='K'
    elif kb[count:count+3]=='AGU' or kb[count:count+3]=='AGC':
        protein+='S'
    elif kb[count:count+3]=='AGA' or kb[count:count+3]=='AGG':
        protein+='R'
    elif kb[count:count+3]=='GUU' or kb[count:count+3]=='GUC' or kb[count:count+3]=='GUA' or kb[count:count+3]=='GUG':
        protein+='V'
    elif kb[count:count+3]=='GCU' or kb[count:count+3]=='GCC' or kb[count:count+3]=='GCA' or kb[count:count+3]=='GCG':
        protein+='A'
    elif kb[count:count+3]=='GAU' or kb[count:count+3]=='GAC':
        protein+='D'
    elif kb[count:count+3]=='GAA' or kb[count:count+3]=='GAG':
        protein+='E'
    elif kb[count:count+3]=='GGU' or kb[count:count+3]=='GGC' or kb[count:count+3]=='GGA' or kb[count:count+3]=='GGG':
        protein+='G'
    else:
        break
    count+=3

print(protein)
