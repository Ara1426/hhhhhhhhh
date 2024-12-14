def malik(mcd):
    ctr=0
    lst=[]
    for i in mcd:
        if len(i)>1 and i[0]==i[-1]:
            ctr+=1
            lst.append(i)
    print("List of words with first and last character same\n", lst)
    return ctr
count=malik(['abc', 'cfc','xyz', 'aba', '1221'])
        
