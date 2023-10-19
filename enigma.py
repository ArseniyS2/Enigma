class Enigma:
    def __init__(self, r1, r2, r3, re, pb, kb):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.re = re
        self.pb = pb
        self.kb = kb
    
    def set_key(self, key):
        self.r1.starting_position(key[0])
        self.r2.starting_position(key[1])
        self.r3.starting_position(key[2])
    
    def set_rings(self, key):
        self.r1.ring_setting(key[0])
        self.r2.ring_setting(key[1])
        self.r3.ring_setting(key[2])

    def encipher(self, letter):
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r3.rotate()
            self.r2.rotate()
            self.r1.rotate()
        elif self.r2.left[0] == self.r2.notch: #historically that was a bug in the enigma
            self.r3.rotate()
            self.r2.rotate()
            self.r1.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r3.rotate()
            self.r2.rotate()
        else:
            self.r3.rotate()
        
        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.re.reflect(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)

        return letter