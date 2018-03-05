# this program will calculate the profile matrix and the consensus of serveral
# DNA squences which have same length.
file = open('dataset.txt','r')

char = file.read(1)
profile = [0 for x in range(4)]
count = 0

while char != '':
    if char == '>':
        file.readline()
        char = file.read(1)
        count = 0
    elif char =='\n':
        char = file.read(1)
    else:
        if len(profile) == 4*count:
            profile.extend([0,0,0,0])
        if char == 'A':
            profile[4*count]+=1
        elif char == 'C':
            profile[4*count+1]+=1
        elif char == 'G':
            profile[4*count+2]+=1
        else:
            profile[4*count+3]+=1
        count+=1
        char = file.read(1)
consensus = ''


for x in range(0,count):
    max_ = profile[4*x]
    s = 'A'
    if max_<profile[4*x+1]:
        max_ = profile[4*x+1]
        s = 'C'
    if max_<profile[4*x+2]:
        max_ = profile[4*x+2]
        s = 'G'
    if max_<profile[4*x+3]:
        max_ = profile[4*x+3]
        s = 'T'
    consensus+=s
print(consensus+' ')

str_profile = ''
str_profile+='A: '
for x in range(0,count):
    str_profile+=str(profile[4*x])+' '

str_profile+='\nC: '
for x in range(0,count):
    str_profile+=str(profile[4*x+1])+' '

str_profile+='\nG: '
for x in range(0,count):
    str_profile+=str(profile[4*x+2])+' '

str_profile+='\nT: '
for x in range(0,count):
    str_profile+=str(profile[4*x+3])+' '
print(str_profile)
