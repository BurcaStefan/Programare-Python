def Intersection(A,B):
    result=[]
    for nr1 in A:
        for nr2 in B:
           if nr1==nr2:
               result.append(nr1)
    return sorted(result)

def Reunion(A,B):
    result=[]
    for nr in A:
        result.append(nr)
    for nr in B:
        result.append(nr)
    return sorted(set(result))
    

list1=[1,3,4,5,7,8,9,10,11,13,15]
list2=[2,4,5,6,8,9,10,12,14]

AintersectedB=Intersection(list1,list2)
AreunitedB=Reunion(list1,list2)
print("Intersectia: ", AintersectedB)
print("Reuniunea: ", AreunitedB)