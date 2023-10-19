class Rotor:
    def __init__(self, rotor_num, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = rotor_num
        self.notch = notch
    def forward(self, signal): #signal is an index
        letter = self.right[signal]
        return self.left.find(letter)
    
    def backward(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)
    
    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def starting_position(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)
    
    def ring_setting(self, n):
        self.rotate(n-1, forward=False)
        #adjusting turnover notch
        new_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(new_notch - n) % 26]

    
