def count_unique_and_duplicates(list):
    unique_elements = set(list)
    num_unique = len(unique_elements)
    num_duplicates = len(list) - num_unique
    return (num_unique, num_duplicates)

list = [1, 2, 2, 3, 4, 4, 4, 5]
print(count_unique_and_duplicates(list))