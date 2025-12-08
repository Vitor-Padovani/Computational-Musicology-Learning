class musicAnalyzer:
    scale = ('C', ('C#', 'D-'),
                'D', ('D#', 'E-'),
                'E',
                'F', ('F#', 'G-'),
                'G', ('G#', 'A-'),
                'A', ('A#', 'B-'),
                'B')
    
    def __init__(self):
        pass

    def flip_enharmonic(self, note: str):
        inNote = note[0]
        acc = note[1:] if len(note) > 1 else None

        if acc == None:
            return note
        elif acc[0] == '#':
            result = self.scale[(self.scale.index(inNote) + len(acc)) % len(self.scale)]
        elif acc[0] == '-':
            result = self.scale[(self.scale.index(inNote) - len(acc)) % len(self.scale)]
        
        if len(result) > 1:
            if note in result:
                return result[not result.index(note)]
            else:
                return result[0] # Returns # version of distant acc
        
        return result

    def are_notes_equal(self, note1: str, note2: str):
        if note1 == note2:
            return True
        
        note1enharmonic = self.flip_enharmonic(note1)
        note2enharmonic = self.flip_enharmonic(note2)

        if note1enharmonic == note2enharmonic:
            return True
        elif note1enharmonic == self.flip_enharmonic(note2enharmonic):
            return True
        else:
            return False
    
    def note_index(self, note: str):
        for i, n in enumerate(self.scale):
            if len(n) > 1:
                if self.are_notes_equal(note, n[0]):
                    return i
            else:
                if self.are_notes_equal(note, n):
                    return i

    def note_distance(self, note1: str, note2: str):
        return self.note_index(note2) - self.note_index(note1)
        
    def transpose(self, seq: str, t: int):
        seq = seq.split(' ')
        transposed = []

        for note in seq:
            t_note = self.scale[(self.note_index(note) + t) % len(self.scale)]
            t_note = t_note[0] if len(t_note) > 1 else t_note
            transposed.append(t_note)
        
        return ' '.join(transposed)
    
    def is_sequence_equivalent(self, seq1: str, seq2: str):
        seq1Notes = seq1.split(' ')
        seq2Notes = seq2.split(' ')

        if len(seq1Notes) != len(seq2Notes):
            return False
        
        seqDistance = self.note_distance(seq1Notes[0], seq2Notes[0])
        t_seq2 = self.transpose(seq2, -seqDistance).split(' ')

        for i in range(len(seq1Notes)):
            if not self.are_notes_equal(seq1Notes[i], t_seq2[i]):
                return False
            
        return True

analyzer = musicAnalyzer()

assert analyzer.flip_enharmonic('E-') == 'D#'
assert analyzer.flip_enharmonic('E--') == 'D'
assert analyzer.flip_enharmonic('B#') == 'C'
assert analyzer.flip_enharmonic('E##') == 'F#'
assert analyzer.flip_enharmonic('C') == 'C'
assert analyzer.flip_enharmonic('G#') == 'A-'

assert analyzer.are_notes_equal('C', 'C') is True
assert analyzer.are_notes_equal('C#', 'D-') is True
assert analyzer.are_notes_equal('F##', 'G') is True
assert analyzer.are_notes_equal('C----', 'A-') is True
assert analyzer.are_notes_equal('C----', 'G#') is True
assert analyzer.are_notes_equal('C', 'D') is False


assert analyzer.note_index('C') == 0
assert analyzer.note_index('D#') == 3
assert analyzer.note_index('F-') == 4
assert analyzer.note_index('B') == 11

assert analyzer.note_distance('C', 'C') == 0
assert analyzer.note_distance('C', 'D') == 2
assert analyzer.note_distance('D###', 'F#') == 1
assert analyzer.note_distance('B-', 'C') == -10

assert analyzer.transpose('C D', 2) == 'D E'
assert analyzer.transpose('C D E-', 5) == 'F G G#'
assert analyzer.transpose('B B# D- C-', -1) == 'A# B C A#'

assert analyzer.is_sequence_equivalent('C D', 'D-- E--') is True
assert analyzer.is_sequence_equivalent('C D', 'D E') is True
assert analyzer.is_sequence_equivalent('G C E- G', 'F# B E-- G-') is True
assert analyzer.is_sequence_equivalent('C E G#', 'C F- G') is False
