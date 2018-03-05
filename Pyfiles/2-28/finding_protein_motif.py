#!/usr/bin/emv python3

# import urllib library to read fasta format from uniprot.org
def read_protein_sequence(uniprot):

    import urllib.request

    fl = urllib.request.urlopen("http://www.uniprot.org/uniprot/"+uniprot+".fasta")
    fl.readline()
    seq = ""
    for line in fl:
        seq+=line.decode().strip()
    return seq

# read uniprot id from files
def read_uniprot_id(filepath):

    fl = open(filepath,"r")

    for accession in fl:

        yield accession.strip()
    
# find the indexs of the specific motif from proteins
def find_index_protein_motif(filepath,motif):

    import re

    #read uniprot id from file
    uniprot_ids = read_uniprot_id(filepath)
    
    for _id in uniprot_ids:
        
        seq = read_protein_sequence(_id)
        index = ''
        count = 0


        for match in re.finditer(motif,seq):
            index+=str(match.start()+1)+" "

        if index!='':
            print(index)
            

        
if __name__ == "__main__":

    find_index_protein_motif("dataset.txt",r'(?=N[^P][ST][^P])')
    
