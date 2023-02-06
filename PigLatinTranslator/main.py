import tkinter as tk
from tkinter import filedialog

def translate_to_pig_latin(word):
    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        return word + 'way'
    else:
        for i in range(1, len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'

def translate_file():
    input_file = filedialog.askopenfilename(title="Select a text document to translate", filetypes=(("Text files", ".txt"), ("All files", ".")))
    output_file = filedialog.asksaveasfilename(title="Select a text document to output translated words", defaultextension=".txt", filetypes=(("Text files", ".txt"), ("All files", ".")))

    with open(input_file, 'r') as file_in:
        words = file_in.read().split()

    translated_words = [translate_to_pig_latin(word) for word in words]

    with open(output_file, 'w') as file_out:
        file_out.write(' '.join(translated_words))

root = tk.Tk()
root.title("Pig Latin Translator (2023 By  )")

translate_button = tk.Button(root, text="Translate a text file", command=translate_file)
translate_button.pack()

root.mainloop()