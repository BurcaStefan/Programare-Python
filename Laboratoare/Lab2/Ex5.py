def ispalindrom(nr):
    aux=nr
    palin=0
    while nr>0:
        palin=palin*10+nr%10
        nr=nr//10
    
    if aux==palin:
        print(aux, " este palindrom!")
    else:
        print(aux, " nu este palindrom!")
    
number=int(input())
ispalindrom(number)