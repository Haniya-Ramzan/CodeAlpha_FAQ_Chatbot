# 🏥 MediCare FAQ Chatbot

## CodeAlpha Artificial Intelligence Internship — Task 2

A Python-based FAQ chatbot developed as part of the **CodeAlpha Artificial Intelligence Internship**.

The MediCare FAQ Chatbot uses **Natural Language Processing (NLP)** and **TF-IDF with Cosine Similarity** to understand a user's question and find the most relevant answer from a predefined FAQ dataset.

The project also includes a clean and interactive **Tkinter graphical user interface (GUI)** for chatting with the assistant.

---

## 📌 Project Overview

The MediCare FAQ Chatbot is designed to answer frequently asked questions related to a hospital.

Instead of using fixed keyword-based responses, the chatbot preprocesses the user's question and compares it with the available FAQ questions using **TF-IDF vectorization and Cosine Similarity**.

The FAQ with the highest similarity score is selected and its corresponding answer is displayed to the user.

---

## 🎯 Objectives

The main objectives of this project are:

- Collect and organize hospital-related FAQs.
- Preprocess text using Natural Language Processing.
- Convert FAQ questions into numerical TF-IDF vectors.
- Compare the user's question with the FAQ dataset.
- Use Cosine Similarity to identify the most relevant FAQ.
- Display the best matching answer.
- Provide an interactive graphical chatbot interface.

---

## ✨ Features

- 🏥 MediCare Hospital FAQ assistant
- 🤖 AI-based FAQ matching
- 🧠 Natural Language Processing using NLTK
- 📊 TF-IDF text vectorization
- 🔎 Cosine Similarity matching
- 💬 Interactive Tkinter chatbot interface
- ⚡ Quick question buttons
- 📋 Clear chat functionality
- ⌨️ Enter key support for sending questions
- 🔄 Similarity threshold for handling unmatched questions
- 📁 FAQ data stored separately in JSON format

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| NLTK | Text preprocessing and tokenization |
| Scikit-learn | TF-IDF and Cosine Similarity |
| Tkinter | Graphical User Interface |
| JSON | FAQ dataset storage |
| Regular Expressions | Text cleaning |

---

## 🧠 How the Chatbot Works

The chatbot follows these main steps:

```text
User enters a question
        ↓
Text preprocessing
        ↓
Lowercase conversion
        ↓
Special character removal
        ↓
NLTK tokenization
        ↓
TF-IDF vectorization
        ↓
Cosine Similarity calculation
        ↓
Find highest similarity score
        ↓
Check similarity threshold
        ↓
Return best matching FAQ answer
        ↓
Display response in GUI
