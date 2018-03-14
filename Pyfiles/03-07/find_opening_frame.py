#!usr/pyhton/env python3

def find_reading_frames(seq):

    import Transcribing_DNA_into_RNA
    import Translating_RNA_into_Protein
    import compute_stand_DNA    
    
    pos_frame = Transcribing_DNA_into_RNA.DNA_into_RNA(seq)
    neg_frame = Transcribing_DNA_into_RNA.DNA_into_RNA(compute_stand_DNA.compute_stand_DNA(seq))

    print(neg_frame)
    
    ORF_list = []
    
    for count in range(0,3):
        startpoint = []
        while count < len(pos_frame):
            if pos_frame[count:count+3] == 'AUG':
                startpoint.append(count);
            elif pos_frame[count:count+3] == 'UAA' or pos_frame[count:count+3] == 'UAG' or pos_frame[count:count+3] == 'UGA':
                for point in startpoint:
                    ORF = Translating_RNA_into_Protein.mRNA_into_protein(pos_frame[point:])
                    if ORF not in ORF_list:
                        ORF_list.append(ORF)
            count += 3
    
    for count in range(0,3):
        startpoint = []
        while count < len(neg_frame): 
            if neg_frame[count:count+3] == 'AUG':
                startpoint.append(count);
            elif neg_frame[count:count+3] == 'UAA' or neg_frame[count:count+3] == 'UAG' or neg_frame[count:count+3] == 'UGA':
                for point in startpoint:
                    ORF = Translating_RNA_into_Protein.mRNA_into_protein(neg_frame[point:])
                    if ORF not in ORF_list:
                        ORF_list.append(ORF)
            count += 3
    return ORF_list
            
if __name__== "__main__":
    
    ORF_list = find_reading_frames(input("enter DNA seq:\n"))
    
    for ORF in ORF_list:
        print(ORF)
