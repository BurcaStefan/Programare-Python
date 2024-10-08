number=int(input())
binary=bin(number)
count=0

for ch in binary:
    if ch=='1':
        count+=1
        
print("Numarul ", number, " are ", count, "biti de 1 in componenta sa")