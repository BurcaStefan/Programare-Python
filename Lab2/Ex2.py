string=input()
count=0

for ch in string:
    if ch in "AEIOUaeiou":
        count+=1

print("In sirul dat ", string, " vocalele apar de ", count, "ori")