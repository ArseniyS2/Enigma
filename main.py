from plugboard import Plugboard
from Rotors import Rotor
from Reflector import Reflector
from Keyboard import Keyboard
from enigma import Enigma
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
KB = Keyboard()

# print(ENIGMA.encipher("A"))
if __name__ == "__main__":
    plain_text = input("Write your text to encrypt: ").upper()
    message_key = input("Write a message key (starting position for rotor, ABC): ")
    ring_setting1 = int(input("Write a ring setting for 1st rotor (1): "))
    ring_setting2 = int(input("Write a ring setting for 2nd rotor (1): "))
    ring_setting3 = int(input("Write a ring setting for 3rd rotor (1): "))
    plugboard = input("Write a plugboard if necessary (AB CD RK) up to ten pairs: ") #creating plugboard
    plugboard = plugboard.split()
    PB = Plugboard(plugboard)
    ENIGMA = Enigma(I, II, III, A, PB, KB)
    ENIGMA.set_key(message_key)
    ENIGMA.set_rings((ring_setting1, ring_setting2, ring_setting3))
    cipher_text = ""
    for letter in plain_text:
        cipher_text += ENIGMA.encipher(letter)
    print(cipher_text)