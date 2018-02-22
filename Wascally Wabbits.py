def countPair(month, produce):
    if  month > 2:
        return countPair(month-1,produce)+ produce*countPair(month-2,produce)
    else:
        return 1
kb1 = int(input('please enter month: '))
kb2 = int(input('please enter number of produce: '))

print(countPair(kb1,kb2))
