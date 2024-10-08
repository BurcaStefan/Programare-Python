string=input()
number=0

for ch in string:
    if ch.isdigit():
        number=number*10+int(ch)
    if number>0 and ch.isdigit()==False:
        break

print("In sirul dat, primul numar este ", number)