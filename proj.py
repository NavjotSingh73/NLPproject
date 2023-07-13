import tkinter as tk
from tkinter import scrolledtext
import spacy


nlp = spacy.load('en_core_web_sm')

def process_text():
    
    text = input_text.get("1.0", tk.END).strip()

    
    doc = nlp(text)

    
    clear_tokens()

    
    for token in doc:
    
        lemma = token.lemma_

        # Get the part of speech tag of the token
        pos = spacy.explain(token.pos_)

        # Create a button for each token
        token_button = tk.Button(output_frame, text=token.text, bg="white", fg="red")
        token_button.config(command=lambda btn=token_button, txt=token.text, lma=lemma, p=pos: display_description(btn, txt, lma, p))
        token_button.pack(side='left')

def display_description(button, token_text, lemma, pos):
    # Get the token's description
    description = f"Token: {token_text}\nLemma: {lemma}\nPart of Speech: {pos}"

    # Update the description text box
    description_text.delete("1.0", tk.END)
    description_text.insert(tk.END, description)

def clear_tokens():
    # Destroy the existing buttons
    for widget in output_frame.winfo_children():
        widget.destroy()

# Create the GUI
window = tk.Tk()
window.title("Token Processor")

# Input text
input_label = tk.Label(window, text="Input Text:")
input_label.pack()
input_text = scrolledtext.ScrolledText(window, height=10)
input_text.pack()


process_button = tk.Button(window, text="Process", command=process_text)
process_button.pack()


output_frame = tk.Frame(window)
output_frame.pack()


description_label = tk.Label(window, text="Token Description:")
description_label.pack()
description_text = scrolledtext.ScrolledText(window, height=10)
description_text.pack()


window.mainloop()
