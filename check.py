import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


# Sample list of safe words
unsafe_words = ["adult",
    "violence",
    "hate",
    "pornography",
    "gambling",
    "drugs",
    "terrorism",
    "harmful",
    "illegal",
    "weapon",
    "fraud",
    "phishing",
    "malware",
    "hacking",
    "exploit",
    "suicide",
    "self-harm",
    "discrimination",
    "harassment",
    "racism",
    "sexism",
    "hate speech",
    "threat",
    "abuse",
    "bullying",
    "extremism",
    "vulgar",
    "profanity",
    "obscenity",
    "nudity",
    "gore",
    "injury",
    "violence"]

# Initialize the Tkinter window
root = tk.Tk()
root.title("Text File Analysis")

# Function to open a text file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
        text_entry.delete(1.0, tk.END)
        text_entry.insert(tk.END, text)

# Function to create a word cloud
def generate_word_cloud():
    text = text_entry.get(1.0, tk.END)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# Function to create a frequency chart
def generate_frequency_chart():
    text = text_entry.get(1.0, tk.END)
    words = text.split()
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(10)

    top_words = [word for word, _ in most_common_words]
    word_counts = [count for _, count in most_common_words]

    plt.bar(top_words, word_counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()

# Function to categorize words as safe or unsafe
def categorize_words():
    text = text_entry.get(1.0, tk.END)
    words = text.split()
    categorized_words = []
    for word in words:
        if word.lower() in unsafe_words:
            categorized_words.append(f"{word} (unsafe)")
        else:
            categorized_words.append(f"{word} (safe)")
    categorized_text = " ".join(categorized_words)
    text_entry.delete(1.0, tk.END)
    text_entry.insert(tk.END, categorized_text)
def entity_recognition():
    text = text_entry.get(1.0, tk.END)
    # Process the text with spaCy
    doc = nlp(text)

    # Extract and print entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    entity_text = "\n".join([f"Entity: {text}, Label: {label}" for text, label in entities])
    text_entry.delete("1.0", "end")
    text_entry.insert("1.0", entity_text)
    

# Function to find and display heading with "system" keyword
def find_and_display_heading():
    text = text_entry.get(1.0, tk.END)
    lines = text.split("\n")
    for line in lines:
        if "system" in line.lower():
            text_entry.delete(1.0, tk.END)
            text_entry.insert(tk.END, line)
            break

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)

# Create GUI components
text_entry = tk.Text(root, wrap=tk.WORD, height=20, width=50)
text_entry.pack(padx=10, pady=10)
word_cloud_button = tk.Button(root, text="Generate Word Cloud", command=generate_word_cloud, bg="blue", fg="white")
word_cloud_button.pack(pady=5)
frequency_chart_button = tk.Button(root, text="Generate Frequency Chart", command=generate_frequency_chart, bg="green", fg="white")
frequency_chart_button.pack(pady=5)
categorize_button = tk.Button(root, text="Categorize Words", command=categorize_words, bg="orange", fg="white")
categorize_button.pack(pady=5)
heading_button = tk.Button(root, text="System Name", command=find_and_display_heading, bg="red", fg="white")
heading_button.pack(pady=5)
Entity_button= tk.Button(root, text="Entity Recognition", command=entity_recognition, bg="pink", fg="white")
Entity_button.pack(pady=5)
# Start the main loop
root.mainloop()
