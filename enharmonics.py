def flip_enharmonic(note: str):
    scale = ('C', ('C#', 'D-'),
             'D', ('D#', 'E-'),
             'E',
             'F', ('F#', 'G-'),
             'G', ('G#', 'A-'),
             'A', ('A#', 'B-'),
             'B')
    
    inNote = note[0]
    acc = note[1:] if len(note) > 1 else None

    if acc == None:
        return note
    elif acc[0] == '#':
        result = scale[(scale.index(inNote) + len(acc)) % len(scale)]
    elif acc[0] == '-':
        result = scale[(scale.index(inNote) - len(acc)) % len(scale)]
    
    if len(result) > 1:
        if note in result:
            return result[not result.index(note)]
        else:
            return result[0]
    

    return result

print(flip_enharmonic('E-'))
print(flip_enharmonic('E--'))
print(flip_enharmonic('B#'))
print(flip_enharmonic('E##'))
print(flip_enharmonic('G#'))
print(flip_enharmonic('C'))
