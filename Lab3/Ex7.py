def Ispalindrom(nr):
    aux=nr
    palin=0
    while nr>0:
        palin=palin*10+nr%10
        nr=nr//10
    
    if aux==palin:
        return palin
    else:
        return 0

def Palindromtuple(list):
    x=0
    y=0
    for nr in list:
        palindrom=Ispalindrom(nr)
        if palindrom!=0:
            x+=1
            if palindrom>y:
                y=palindrom
    return x,y
            
listofnumbers=[121,345,674,33,909]
print(Palindromtuple(listofnumbers))