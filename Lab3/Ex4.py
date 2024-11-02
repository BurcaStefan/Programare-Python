def Compose(notes, moves, start):
    result = []
    position = start

    result.append(notes[position])

    for move in moves:
        position = (position + move) % len(notes)  
        result.append(notes[position])

    return result

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2

song = Compose(notes, moves, start)
print(song)