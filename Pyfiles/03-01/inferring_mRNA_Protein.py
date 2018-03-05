#!usr/bin/env python3

def inferring_mRNA_Protein(seq):
    RNA_codon_table = {
                        "A":4,
                        "C":2,
                        "D":2,
                        "E":2,
                        "F":2,
                        "G":4,
                        "H":2,
                        "I":3,
                        "K":2,
                        "L":6,
                        "M":1,
                        "N":2,
                        "P":4,
                        "Q":2,
                        "R":6,
                        "S":6,
                        "T":4,
                        "V":4,
                        "W":1,
                        "Y":2,
                        }

    num = 1
    
    for char in seq:

        num *= RNA_codon_table.get(char)
        if num>1000000:
            num = num % 1000000

    return num*3 % 1000000
        
if __name__ == "__main__":

    seq = input("enter the protein string:")
    print(inferring_mRNA_Protein(seq))
