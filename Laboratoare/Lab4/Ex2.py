def char_count(text):
    count_dict = {}
    
    for char in text:
        count_dict[char] = count_dict.get(char, 0) + 1
    
    return count_dict

text="Ana are mere."
print(char_count(text))