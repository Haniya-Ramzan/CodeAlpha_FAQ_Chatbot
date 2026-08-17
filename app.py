import json
import re
import tkinter as tk
from tkinter import scrolledtext

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# NLTK DATA
# ============================================================

nltk.download("punkt_tab", quiet=True)


# ============================================================
# LOAD FAQ DATA
# ============================================================

with open("faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


# ============================================================
# TEXT PREPROCESSING
# ============================================================

def preprocess_text(text):
    """
    Clean and tokenize text using NLTK.
    """

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    tokens = nltk.word_tokenize(text)

    return " ".join(tokens)


# ============================================================
# PREPROCESS FAQ QUESTIONS
# ============================================================

faq_questions = [
    preprocess_text(faq["question"])
    for faq in faqs
]


# ============================================================
# TF-IDF
# ============================================================

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(faq_questions)


# ============================================================
# FIND BEST FAQ RESPONSE
# ============================================================

def get_response(user_question):
    """
    Find the FAQ most similar to the user's question
    using cosine similarity.
    """

    processed_question = preprocess_text(user_question)

    user_vector = vectorizer.transform(
        [processed_question]
    )

    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarities.argmax()

    best_score = similarities[0][best_match_index]

    # Minimum similarity required for a meaningful answer
    if best_score < 0.20:
        return (
            "I'm sorry, I couldn't find a suitable answer "
            "to your question.\n\n"
            "Please contact the MediCare Hospital reception "
            "for further assistance."
        )

    return faqs[best_match_index]["answer"]


# ============================================================
# SEND MESSAGE
# ============================================================

def send_message(event=None):

    user_question = user_input.get().strip()

    if not user_question or user_question == "Type your question here...":
        return

    # Display user message
    add_user_message(user_question)

    # Get chatbot response
    response = get_response(user_question)

    # Display chatbot response
    root.after(
        250,
        lambda: add_bot_message(response)
    )

    # Clear input
    user_input.delete(0, tk.END)


# ============================================================
# ADD USER MESSAGE
# ============================================================

def add_user_message(message):

    chat_area.configure(state="normal")

    chat_area.insert(
        tk.END,
        "\n"
    )

    chat_area.insert(
        tk.END,
        "You\n",
        "user_name"
    )

    chat_area.insert(
        tk.END,
        message + "\n",
        "user_message"
    )

    chat_area.configure(state="disabled")

    chat_area.see(tk.END)


# ============================================================
# ADD BOT MESSAGE
# ============================================================

def add_bot_message(message):

    chat_area.configure(state="normal")

    chat_area.insert(
        tk.END,
        "\n"
    )

    chat_area.insert(
        tk.END,
        "MediCare Assistant\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        message + "\n",
        "bot_message"
    )

    chat_area.configure(state="disabled")

    chat_area.see(tk.END)


# ============================================================
# CLEAR CHAT
# ============================================================

def clear_chat():

    chat_area.configure(state="normal")

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.configure(state="disabled")

    show_welcome_message()


# ============================================================
# WELCOME MESSAGE
# ============================================================

def show_welcome_message():

    chat_area.configure(state="normal")

    chat_area.insert(
        tk.END,
        "\n"
    )

    chat_area.insert(
        tk.END,
        "MediCare Assistant\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        "Hello! Welcome to MediCare FAQ Assistant.\n\n"
        "I can help you with questions about:\n\n"
        "• Hospital opening hours\n"
        "• Appointments\n"
        "• Departments\n"
        "• Emergency services\n"
        "• Doctors and specialists\n"
        "• Laboratory services\n"
        "• ICU and operation theatre\n"
        "• Patient visits\n\n"
        "How can I help you today?",
        "bot_message"
    )

    chat_area.configure(state="disabled")

    chat_area.see(tk.END)


# ============================================================
# SUGGESTION BUTTONS
# ============================================================

def ask_suggestion(question):

    user_input.delete(
        0,
        tk.END
    )

    user_input.insert(
        0,
        question
    )

    send_message()


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "MediCare FAQ Assistant"
)

root.geometry(
    "850x700"
)

root.minsize(
    700,
    600
)

root.configure(
    bg="#f4f7fb"
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#0b6e8e",
    height=85
)

header.pack(
    fill=tk.X
)

header.pack_propagate(
    False
)


# Hospital icon
icon_label = tk.Label(
    header,
    text="🏥",
    font=("Arial", 28),
    bg="#0b6e8e",
    fg="white"
)

icon_label.pack(
    side=tk.LEFT,
    padx=(25, 10)
)


# Header text container
header_text = tk.Frame(
    header,
    bg="#0b6e8e"
)

header_text.pack(
    side=tk.LEFT,
    pady=10
)


title_label = tk.Label(
    header_text,
    text="MediCare FAQ Assistant",
    font=("Arial", 20, "bold"),
    bg="#0b6e8e",
    fg="white"
)

title_label.pack(
    anchor="w"
)


subtitle_label = tk.Label(
    header_text,
    text="AI-powered hospital information assistant",
    font=("Arial", 10),
    bg="#0b6e8e",
    fg="#d9f3fa"
)

subtitle_label.pack(
    anchor="w"
)


# Online status
status_label = tk.Label(
    header,
    text="● Online",
    font=("Arial", 10, "bold"),
    bg="#0b6e8e",
    fg="#d9f3fa"
)

status_label.pack(
    side=tk.RIGHT,
    padx=25
)


# ============================================================
# CHAT CONTAINER
# ============================================================

chat_container = tk.Frame(
    root,
    bg="#f4f7fb",
    height=390
)

chat_container.pack(
    fill=tk.X,
    padx=25,
    pady=(20, 10)
)

chat_container.pack_propagate(False)


# ============================================================
# CHAT AREA
# ============================================================

chat_area = scrolledtext.ScrolledText(
    chat_container,
    wrap=tk.WORD,
    font=("Arial", 11),
    bg="white",
    fg="#263238",
    relief=tk.FLAT,
    borderwidth=0,
    padx=20,
    pady=15,
    spacing1=5,
    spacing3=8
)

chat_area.pack(
    fill=tk.BOTH,
    expand=True
)


# ============================================================
# CHAT TEXT STYLES
# ============================================================

chat_area.tag_configure(
    "user_name",
    font=("Arial", 10, "bold"),
    foreground="#0b6e8e"
)

chat_area.tag_configure(
    "user_message",
    font=("Arial", 11),
    foreground="#263238"
)

chat_area.tag_configure(
    "bot_name",
    font=("Arial", 10, "bold"),
    foreground="#167c3a"
)

chat_area.tag_configure(
    "bot_message",
    font=("Arial", 11),
    foreground="#263238"
)

chat_area.configure(
    state="disabled"
)


# ============================================================
# SUGGESTION AREA
# ============================================================

suggestion_label = tk.Label(
    root,
    text="Quick questions",
    font=("Arial", 10, "bold"),
    bg="#f4f7fb",
    fg="#607d8b"
)

suggestion_label.pack(
    anchor="w",
    padx=30
)


suggestion_frame = tk.Frame(
    root,
    bg="#f4f7fb"
)

suggestion_frame.pack(
    fill=tk.X,
    padx=25,
    pady=8
)


# Suggestion buttons

button_style = {
    "font": ("Arial", 9),
    "bg": "white",
    "fg": "#0b6e8e",
    "activebackground": "#e3f5fa",
    "activeforeground": "#07566e",
    "relief": tk.FLAT,
    "bd": 0,
    "padx": 10,
    "pady": 6,
    "cursor": "hand2"
}


appointment_button = tk.Button(
    suggestion_frame,
    text="Appointments",
    command=lambda: ask_suggestion(
        "How can I book an appointment?"
    ),
    **button_style
)

appointment_button.pack(
    side=tk.LEFT,
    padx=(0, 8)
)


hours_button = tk.Button(
    suggestion_frame,
    text="Opening Hours",
    command=lambda: ask_suggestion(
        "What are the hospital opening hours?"
    ),
    **button_style
)

hours_button.pack(
    side=tk.LEFT,
    padx=8
)


emergency_button = tk.Button(
    suggestion_frame,
    text="Emergency",
    command=lambda: ask_suggestion(
        "Does the hospital have an emergency department?"
    ),
    **button_style
)

emergency_button.pack(
    side=tk.LEFT,
    padx=8
)


departments_button = tk.Button(
    suggestion_frame,
    text="Departments",
    command=lambda: ask_suggestion(
        "What departments are available at the hospital?"
    ),
    **button_style
)

departments_button.pack(
    side=tk.LEFT,
    padx=8
)


# ============================================================
# INPUT AREA
# ============================================================

input_container = tk.Frame(
    root,
    bg="#f4f7fb"
)

input_container.pack(
    fill=tk.X,
    padx=25,
    pady=(5, 20)
)


# Visible input box
user_input = tk.Entry(
    input_container,
    font=("Arial", 13),
    bg="white",
    fg="#263238",
    insertbackground="#0b6e8e",
    relief=tk.SOLID,
    bd=1
)

user_input.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=12,
    padx=(0, 10)
)


# Placeholder text
user_input.insert(
    0,
    "Type your question here..."
)

user_input.config(
    fg="#90a4ae"
)


# Remove placeholder when user clicks
def clear_placeholder(event):

    if user_input.get() == "Type your question here...":
        user_input.delete(0, tk.END)
        user_input.config(
            fg="#263238"
        )


user_input.bind(
    "<FocusIn>",
    clear_placeholder
)
# Send button
send_button = tk.Button(
    input_container,
    text="Send  ➤",
    font=("Arial", 11, "bold"),
    bg="#0b6e8e",
    fg="white",
    activebackground="#07566e",
    activeforeground="white",
    relief=tk.FLAT,
    bd=0,
    padx=22,
    pady=10,
    cursor="hand2",
    command=send_message
)

send_button.pack(
    side=tk.RIGHT
)


# ============================================================
# CLEAR CHAT BUTTON
# ============================================================

clear_button = tk.Button(
    header,
    text="Clear",
    font=("Arial", 9),
    bg="#0b6e8e",
    fg="white",
    activebackground="#07566e",
    activeforeground="white",
    relief=tk.FLAT,
    bd=0,
    cursor="hand2",
    command=clear_chat
)

clear_button.pack(
    side=tk.RIGHT,
    padx=(0, 15)
)


# ============================================================
# ENTER KEY
# ============================================================

user_input.bind(
    "<Return>",
    send_message
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

show_welcome_message()


# Automatically put cursor in input box
user_input.focus()


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()