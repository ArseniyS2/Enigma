class Reflector:
    def __init__(self, rotor_num):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = rotor_num
    def reflect(self, signal): #signal is an index
        letter = self.right[signal]
        return self.left.find(letter)
    