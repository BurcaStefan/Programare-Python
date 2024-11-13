from itertools import zip_longest

def Combinelists(*lists):
    return list(zip_longest(*lists))

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = Combinelists(list1, list2, list3)
print(result)
