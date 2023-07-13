# Project Name

Text Processing with POS Tagging and NER in GUI

## Description

This Python project utilizes the power of natural language processing and graphical user interface to tokenize, lemmatize, describe part-of-speech (POS), and run named entity recognition (NER) on a given text. The project leverages the Spacy library for text processing tasks and Tkinter for creating an interactive GUI.

The program accepts input in the form of text, which can be a document, an article, or any other textual content. The main objectives of the project are to tokenize the text, lemmatize the tokens, provide POS tags for each token, and identify named entities within the text.

Spacy, a popular natural language processing library, is utilized to analyze and process the input text. It performs tasks such as tokenization, which breaks the text into individual tokens, lemmatization, which reduces each token to its base or root form, and POS tagging, which assigns grammatical labels to each token based on its role in the sentence.

In addition to tokenization, lemmatization, and POS tagging, the program also runs NER on the text. NER aims to identify and classify named entities such as persons, organizations, locations, dates, and more within the text. Spacy's NER functionality is utilized to accomplish this task.

To enhance user experience, the project incorporates Tkinter, a standard GUI toolkit, to display the output. Tkinter provides a range of tools and widgets for building GUI elements such as windows, frames, buttons, and labels. These elements are utilized to present the tokenized text, lemmatized tokens, POS tags, and named entities in an interactive and visually appealing manner.

## Features

- Accepts text input and processes it using Spacy's natural language processing capabilities.
- Performs tokenization to break the text into individual tokens.
- Lemmatizes the tokens to reduce them to their base or root form.
- Provides POS tags for each token, describing their grammatical role.
- Runs NER on the text to identify and classify named entities.
- Creates an interactive GUI using Tkinter to display the processed text and extracted information.
- Provides a user-friendly interface for inputting text and viewing the tokenized text, lemmas, POS tags, and named entities.

## Installation

1. Clone the repository: `git clone https://github.com/NavjotSingh73/NLPproject.git`
2. Navigate to the project directory: `cd your_project`
3. Install the required dependencies: `pip install spacy tkinter` (ensure Spacy is properly installed and has downloaded the necessary language models)
4. Run the main program: `python main.py`

## Usage

1. Launch the application by running `main.py`.
2. Enter the text you want to tokenize, lemmatize, describe POS, and run NER on.
3. Click the "Process Text" button to analyze the input text.
4. The tokenized text, lemmatized tokens, POS tags, and named entities will be displayed in the GUI.
5. Explore the different sections of the GUI to examine the extracted information.
6. Repeat the process with different text inputs as needed.

## Contributing

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please open an issue on the project repository. Feel free to fork the repository and submit pull requests to contribute code changes.

## License

[ License](https://opensource.org/licenses/gnv)
