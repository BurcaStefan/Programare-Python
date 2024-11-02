def Groupbyrhyme(words):
    rhymelist = []

    for word in words:
        addedtogroup = False
        if len(word) >= 2:
            rhyme = word[-2:]

            for group in rhymelist:
                if group[0][-2:] == rhyme:
                    group.append(word)
                    addedtogroup = True
                    break
            
            if not addedtogroup:
                rhymelist.append([word])
    
    return rhymelist

words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = Groupbyrhyme(words)
print(result)
