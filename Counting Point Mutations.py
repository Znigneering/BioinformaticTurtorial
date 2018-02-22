def countHammingDistance(string1,string2):
    hammingdistance = 0
    count = 0
    for x in string1:
        if x != string2[count]:
            hammingdistance+=1
        count+=1
    return hammingdistance

kb1 = input('Please enter the first DNA sequence: ')
kb2 = input('Please enter the second DNA sedquence: ')

print('The Hamming distance is',countHammingDistance(kb1,kb2))
