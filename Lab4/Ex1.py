def list_set_operations(a, b):
    set_a = set(a)
    set_b = set(b)
    
    intersection = set_a & set_b
    reunion = set_a | set_b
    a_minus_b = set_a - set_b
    b_minus_a = set_b - set_a
    
    return [intersection, reunion, a_minus_b, b_minus_a]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(list_set_operations(a, b))