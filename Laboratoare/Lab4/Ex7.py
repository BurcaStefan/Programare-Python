def set_operations(*sets):
    result = {}
    sets = list(sets)
    
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i], sets[j]
            result[f"{a} | {b}"] = a | b
            result[f"{a} & {b}"] = a & b
            result[f"{a} - {b}"] = a - b
            result[f"{b} - {a}"] = b - a
            
    return result

sets = ({1, 2}, {2, 3})
print(set_operations(*sets))