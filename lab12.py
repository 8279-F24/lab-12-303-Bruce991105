from adafruit_circuitplayground import cp
import time

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

def display_morse_code(morse_code_string, unit_length=0.2, color=(0, 255, 0)):
    for symbol in morse_code_string:
        if symbol == '.':
            cp.pixels.fill(color)  # Light up all 10 LEDs
            time.sleep(unit_length)  # Dot duration
            cp.pixels.fill((0, 0, 0))  # Turn off LEDs
            time.sleep(unit_length)  # Space between dot/dash
        elif symbol == '-':
            cp.pixels.fill(color)  # Light up all 10 LEDs
            time.sleep(unit_length * 3)  # Dash duration
            cp.pixels.fill((0, 0, 0))  # Turn off LEDs
            time.sleep(unit_length)  # Space between dot/dash
        elif symbol == ' ':
            time.sleep(unit_length * 3)  # Space between letters
        elif symbol == '   ':
            time.sleep(unit_length * 7)  # Space between words


def filter_sentence(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    # Keep only characters that are lowercase letters, digits, or spaces
    return ''.join([char for char in sentence if char.islower() or char.isdigit() or char == ' '])

def text_to_morse(text):
    morse = []
    words = text.split()
    for word in words:
        morse_word = []
        for char in word:
            if char in morse_code:
                morse_word.append(morse_code[char])
        morse.append(' '.join(morse_word))  # Space between letters is 3 units
    return '   '.join(morse)  # Space between words is 7 units

def main():
    unit_length = float(input("Enter the unit length (0-1 seconds, e.g., 0.2): "))
    red = int(input("Enter red value for color (0-255): "))
    green = int(input("Enter green value for color (0-255): "))
    blue = int(input("Enter blue value for color (0-255): "))
    color = (red, green, blue)
    
    sentence = input("Enter a sentence: ")
    filtered_sentence = filter_sentence(sentence)
    morse_output = text_to_morse(filtered_sentence)
    
    print("Filtered Sentence:", filtered_sentence)
    print("Morse Code:", morse_output)
    display_morse_code(morse_output, unit_length, color)

if __name__ == "__main__":
    main()
