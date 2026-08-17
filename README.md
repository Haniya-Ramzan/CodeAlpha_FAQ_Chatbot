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

📂 Project Structure

CodeAlpha_FAQ_Chatbot/
│
├── app.py
├── faqs.json
├── README.md
└── .gitignore

app.py

Contains the main chatbot application, including:

NLTK preprocessing
FAQ loading
TF-IDF vectorization
Cosine Similarity
Response matching
Tkinter GUI
User interaction
faqs.json

Contains the hospital-related questions and their corresponding answers.

The dataset includes FAQs related to:

Hospital opening hours
Appointments
Emergency services
Hospital departments
Payment methods
Medical reports
ICU
Operation theatre
Specialist doctors
Pediatric care
Patient visits
Diagnostic services
.gitignore

Prevents unnecessary files such as the Python virtual environment from being uploaded to GitHub.

⚙️ Requirements

Make sure Python is installed on your computer.

The project uses the following Python libraries:
nltk
scikit-learn
Tkinter is used for the GUI.

🚀 Installation and Setup
1. Clone the Repository
git clone https://github.com/Haniya-Ramzan/CodeAlpha_FAQ_Chatbot.git
2. Open the Project Folder
cd CodeAlpha_FAQ_Chatbot
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

On Windows PowerShell:

venv\Scripts\activate
5. Install Required Libraries
pip install nltk scikit-learn
6. Run the Application
python app.py
💬 Example Questions

You can ask questions such as:

What are the hospital opening hours?
How can I book an appointment?
Does the hospital have an ICU?
Does the hospital have an emergency department?
What departments are available at the hospital?
Are specialist doctors available?

🔍 Similarity Matching

The chatbot uses:

TF-IDF

TF-IDF converts the FAQ questions and the user's question into numerical vectors based on the importance of words.

Cosine Similarity

Cosine Similarity compares the user's question with all FAQ questions.

The chatbot identifies the FAQ with the highest similarity score.

A minimum similarity threshold is also used. If the similarity score is too low, the chatbot provides a fallback response instead of returning an unrelated answer.

🖥️ User Interface

The chatbot includes a graphical interface built using Tkinter.

The interface provides:

MediCare Hospital branding
Chat conversation area
User and assistant messages
Question input field
Send button
Quick question buttons
Clear chat option
Online status indicator
🧪 Testing

The chatbot was tested using different hospital-related questions.

Example:

User:

What are the hospital opening hours?

Chatbot:

MediCare Hospital is open 24 hours a day, 7 days a week.

Another example:

User:

Does the hospital have an ICU?

Chatbot:

Yes. The hospital has an Intensive Care Unit for patients who require critical care and continuous monitoring.

The chatbot also provides a fallback response when a question does not have a sufficiently similar FAQ match.

🎓 Internship Task

This project was developed as part of:

CodeAlpha Artificial Intelligence Internship

Task 2: FAQ Chatbot

The task focuses on:

FAQ collection
NLP preprocessing
Similarity-based FAQ matching
Cosine Similarity
Chatbot response generation
User interaction through a chatbot interface
👩‍💻 Author

Haniya Ramzan

Artificial Intelligence Intern
CodeAlpha

📜 License
This project was created for educational and internship purposes.



### One important thing before you commit


Your README currently uses your GitHub repository URL:


```text
https://github.com/Haniya-Ramzan/CodeAlpha_FAQ_Chatbot
