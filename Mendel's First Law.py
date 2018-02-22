def count(hd,he,hr,previous,num_of_selections):    
    t = hd+he+hr
    if num_of_selections > 1:
        if previous == 0:
            return (he/t)*(hd/(t-1) + (3/4)*count(hd, he-1,hr,0,num_of_selections-1) + (1/2)*count(hd,he-1,hr,1,num_of_selections-1))
        else:
            return (hr/t)*(hd/(t-1) + (1/2)*count(hd, he,hr-1,0,num_of_selections-1))
    else:
        if previous == 0:
            return he/t
        else:
            return hr/t
def count_probability_dominant_allele(hd,he,hr,num_of_selections):
        t = hd+he+hr
        return hd/t + count(hd, he,hr,0,num_of_selections) + count(hd, he,hr,1,num_of_selections)

print(count_probability_dominant_allele(27,19,29,6))
