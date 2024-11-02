def Asciidivizible(listofstrings, flag, x=1):
    list=[]
    finallist=[]
    for string in listofstrings:
        if flag:
            for ch in string:
                if ord(ch)%x==0:
                    list.append(ch)
            finallist+=list
            list.clear()
        if flag==False:
            for ch in string:
                if ord(ch)%x!=0:
                    list.append(ch)
            finallist+=list
            list.clear()
        
    print(finallist)
    
    
Asciidivizible(["test", "hello", "lab"],False,2)