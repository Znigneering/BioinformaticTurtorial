#!/usr/bin/env python

def isOverlap(str1,str2):
    if len(str1)>len(str2):
        return False
    index = 0
    while index<len(str2):
        if str1 == str2[index:index+len(str1)]:
            return True
        index+=1
    return False

if __name__ == '__main__':

    list1 = []
    s = ''
    str1 =''
    str2 =''

    fh = open('dataset.txt','r')

    # read first two sequences from file
    s = fh.readline()
    s = fh.readline()
    while s[0] != '>':
        str1 += s[:len(s)-1]
        s = fh.readline()
    s = fh.readline()
    while s[0] != '>':
        str2 += s[:len(s)-1]
        s = fh.readline()
    # find the all common substring between string1 and string2.
    length = 0
    index_str2 = 0
    while str1 !='':
        if index_str2+length > len(str2):
            if length>2 and str1[:length-1] not in list1:
                list1.append(str1[:length-1])     
            str1 = str1[1:]
            length = 0
            index_str2 = 0
        if str1[0:length] == str2[index_str2:index_str2+length]:
            length+=1
        else:
            index_str2+=1
    # Then, read the new DNA sequence one by one, and try to match the element
    # in the list with the new DNA squence. if not matches, then reduce the
    # length and match again until the element is empty.

    s = fh.readline()
    new = ''
    while s!='' or len(list1)==0:
        if s[0]=='>':
            count = 0
            while count <= len(list1):
                curr = list1.pop(0)
                if isOverlap(curr,new):
                    list1.append(curr)
                count+=1
            new = ''
            s = fh.readline()
        else:
            new += s[:len(s)-1]
            s = fh.readline()
    longest = ''
    for seq in list1:
        if len(longest)<len(seq):
            longest = seq
    print(longest)
    fh.close()
