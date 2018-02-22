filename = input('please enter the filename: ')
file = open(filename,'r')

max_FASTA = ''
max_percent = 0
FASTA = ''
total_num = 0
cg_num = 0

for line in file:
    if line[0] == '>':
        if cg_num > max_percent*total_num:
            max_percent = cg_num/total_num
            max_FASTA = string
        total_num=0
        cg_num=0
        string = line
    else:
        total_num-=1
        for x in line:
            if x=='C' or x=='G':
                cg_num+=1
            total_num+=1
if cg_num > max_percent*total_num:
    max_percent = cg_num/total_num
    max_FASTA = string
print(max_FASTA+str(max_percent*100))
        
    
        

