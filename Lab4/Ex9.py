def function(*args, **keywargs):
    count=0
    keywarg_values = set(keywargs.values())
    
    for arg in args:
        if arg in keywarg_values:
            count += 1
    
    return count

result = function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)