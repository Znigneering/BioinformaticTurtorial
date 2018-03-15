#!usr/python/env

def calculate_protein_mass(seq):
    """
    it going to the mass of the protein string by using hash table
    
    argument:
        seq --- Type: string | Description: protein string
    return:
        weight --- Type: int | Description: the total weight of the protein string
    """
    dic = {
            'A':71.03711,
            'C':103.00919,
            'D':115.02694,
            'E':129.04259,
            'F':147.06841,
            'G':57.02146,
            'H':137.05891,
            'I':113.08406,
            'K':128.09496,
            'L':113.08406,
            'M':131.04049,
            'N':114.04293,
            'P':97.05276,
            'Q':128.05858,
            'R':156.10111,
            'S':87.03203,
            'T':101.04768,
            'V':99.06841,
            'W':186.07931,
            'Y':163.06333}
    weight = 0
    for i in seq:
        weight += dic.get(i)
    return weight

if __name__ == '__main__':
    print(calculate_protein_mass(input('please enter the Protein:')))