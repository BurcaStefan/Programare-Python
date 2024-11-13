def cmmdc(m,n):
    while m!=n:
        if m>n: 
            m = m - n
        else: 
            n = n - m
    return m

nr1=int(input())

while True:
    nr2=int(input())
    
    if nr2<=0:
        print("Numarul este invalid!")
        print("Cmmdc-ul numerelor valide date este: ",nr1)
        break
    
    nr1=cmmdc(nr1,nr2)
