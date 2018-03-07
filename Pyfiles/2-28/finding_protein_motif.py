#!/usr/bin/env python3


def read_protein_sequence(uniprot):
    """
    import urllib library to read fasta format from uniprot.org
    """
    import urllib.request

    fl = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + uniprot +
                                ".fasta")

    fl.readline()
    seq = ""
    for line in fl:
        seq += line.decode().strip()
    return seq


def read_uniprot_id(filepath):
    """
    read uniprot id from files
    """

    fl = open(filepath, "r")

    for accession in fl:
        yield accession.strip()


def find_index_protein_motif(filepath, motif):
    """
    find the indexs of the specific motif from proteins
    """

    import re

    # read uniprot id from file
    uniprot_ids = read_uniprot_id(filepath)

    for _id in uniprot_ids:

        seq = read_protein_sequence(_id)
        index = ''
        count = 0

        for match in re.finditer(motif, seq):
            index += str(match.start() + 1) + " "

        if index != '':
            print(index)


if __name__ == "__main__":

    find_index_protein_motif("dataset.txt", r'(?=N[^P][ST][^P])')
