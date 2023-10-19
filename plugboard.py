#for example: ["AB", "ET", "UG"]
class Plugboard:
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #scrambled variant
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #alphabet
        for pair in pairs:
            a = pair[0]
            b = pair[1]
            pos_a = self.left.find(a)
            pos_b = self.left.find(b)
            self.left = self.left[:pos_a] + b + self.left[pos_a + 1:]
            self.left = self.left[:pos_b] + a + self.left[pos_b + 1:]
    def forward(self, signal): #signal is an index
        letter = self.right[signal]
        return self.left.find(letter)
    
    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)


