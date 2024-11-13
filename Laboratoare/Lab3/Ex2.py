def Primnumber(list):
    nr=[nr for nr in list if len([y for y in range(2,nr//2+1) if nr % y==0])==0]
    print(nr[:])
    
numbers=[8,9,3,5,142093,511,35811,3911,57,47,43,2]
Primnumber(numbers)