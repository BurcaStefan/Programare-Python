def Function(x,*arg):
    alllist=[]
    result=[]
    for list in arg:
        for nr in list:
            alllist.append(nr)
    
    for nr in alllist:
        count=0
        for i in range(len(alllist)):
            if nr==alllist[i]:
                count+=1
        if count==x:
            result.append(nr) 
    return set(result)
    
print(Function(2,[10,20,30,40],[11,22,30,44],[10,23,34]))