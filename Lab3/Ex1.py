def Fibonacci(n):
    if n <= 0:
        return "Numarul nu trebuie sa fie negativ"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fiblist = [0, 1]
    
    for i in range(2, n):
        next_number = fiblist[i-1] + fiblist[i-2]
        fiblist.append(next_number)
    
    return fiblist

nr=int(input())
result = Fibonacci(nr)
print(result)