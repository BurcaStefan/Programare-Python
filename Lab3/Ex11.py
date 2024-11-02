def Sortbythirdchar(tupleslist):
    return sorted(tupleslist, key=lambda x: x[1][2])

tuples = [('abc', 'bcd'), ('abc', 'zza')]
result = Sortbythirdchar(tuples)
print(result)
