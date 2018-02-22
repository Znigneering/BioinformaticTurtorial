#!/usr/bin/env python

def is_k_overlap(s1, s2, k):
    l = min(len(s1), len(s2))
    if l <= k:
        return False
    # negative indices count from the end
    return s1[-k:] == s2[:k]


# executable code should be protected like this so you can import
# the file in another script (to use the functions you've defined)
# without executing everything
if __name__ == '__main__':

    # file is reserved word
    fh = open('dataset.txt','r')

    # list is also a reserved word
    sequences = []

    # accession is the name of the fasta sequence specifier
    accession = ''

    seq = ''
    result = ''

    for line in fh:
        # strip remove newline char/whitespace at end of line
        line = line.strip()
        # startswith is a cleaner way of checking this
        if line.startswith('>') or line.startswith('!'):
            """
            you don't actually do all the pairwise comparisons this way
            it misses checking the last sequence in the for overlaps
            """
            for element in sequences:
                if is_k_overlap(element[1], seq, 3):
                    result+=(element[0] + ' ' + accession + '\n')
                if is_k_overlap(seq, element[1], 3):
                    result+=(accession + ' ' + element[0] + '\n')
            sequences.append([accession, seq])

            seq = ''
            # a slice without and end just means to end of line
            accession = line[1:]
        else:
            seq += line
    print(result)

    """
    I often use this structure for opening file so it automatically closes
    the filehandle

    with open('dataset.txt') as fh:
       code manipulating the file
    """
    fh.close()

