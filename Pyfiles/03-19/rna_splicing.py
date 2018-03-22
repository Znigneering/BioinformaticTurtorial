
def rna_splicing(dna,introns):
    
    exon = ''
    seq = ''
    copy_introns = introns.copy()
    len_seq = 0
    clean = false;
    
    for ch in dna:
        seq += ch
        len_seq += 1
        while copy_introns:
            intron = copy_introns.pop()
            if len(intron) > len_seq and intron[len_seq-1] == seq[len_seq-1]:
                copy_
                
                
    
    
if __name__ == "__main__":
    
    import read_fasta
    
    seqs = [seq[1] for seq in read_fasta.read_fasta('dataset.txt')]
    
    protein = rna_splicing(seqs[0],seqs[1:])
    
    print(protein)

