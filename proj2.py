import tkinter as tk
from tkinter import scrolledtext
import spacy
from textblob import TextBlob

# Load the English language model
nlp = spacy.load('en_core_web_sm')

def process_text():
    # Get the input text from the GUI
    text = input_text.get("1.0", tk.END).strip()

    # Process the text with spaCy for named entity recognition
    doc = nlp(text)
    entities = [(entity.text, entity.label_,spacy.explain(entity.label_)) for entity in doc.ents]

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Display the output
    display_output(entities, sentiment)

def display_output(entities, sentiment):
    # Clear the previous output
    output_text.delete("1.0", tk.END)

    # Display named entities
    output_text.insert(tk.END, "Named Entities:\n")
    for entity, label, label_explain in entities:
        output_text.insert(tk.END, f"{entity} - {label} - {label_explain}\n")

    # Display sentiment analysis
    output_text.insert(tk.END, "\nSentiment Analysis:\n")
    output_text.insert(tk.END, f"Sentiment Score: {sentiment}\n")

# Create the GUI
window = tk.Tk()
window.title("NLP Analysis")

# Input text box
input_label = tk.Label(window, text="Input Text:")
input_label.pack()
input_text = scrolledtext.ScrolledText(window, height=10)
input_text.pack()

# Process button
process_button = tk.Button(window, text="Process", command=process_text)
process_button.pack()

# Output text box
output_label = tk.Label(window, text="Output:")
output_label.pack()
output_text = scrolledtext.ScrolledText(window, height=10)
output_text.pack()

# Run the GUI main loop
window.mainloop()
