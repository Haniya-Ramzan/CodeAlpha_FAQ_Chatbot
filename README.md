# 🏥 MediCare FAQ Chatbot

## CodeAlpha Artificial Intelligence Internship — Task 2

A Python-based FAQ chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

The MediCare FAQ Chatbot uses Natural Language Processing (NLP), TF-IDF vectorization, and Cosine Similarity to identify the most relevant answer to a user's question from a predefined hospital FAQ dataset.

The project also includes an interactive Tkinter graphical user interface (GUI) for a user-friendly chatbot experience.

---

## 📌 Project Overview

The MediCare FAQ Chatbot is designed to answer frequently asked questions related to MediCare Hospital.

The chatbot preprocesses the user's question and the FAQ questions using Natural Language Processing. The processed FAQ questions are converted into TF-IDF vectors, and Cosine Similarity is used to determine which FAQ question is most similar to the user's input.

The answer associated with the best matching FAQ is then displayed to the user through the chatbot interface.

---

## 🎯 Objectives

The main objectives of this project are:

- Collect and organize hospital-related FAQs.
- Preprocess text using Natural Language Processing.
- Tokenize and clean user questions.
- Convert FAQ questions into TF-IDF vectors.
- Compare the user's question with the FAQ dataset.
- Use Cosine Similarity to find the most relevant FAQ.
- Display the best matching answer to the user.
- Provide an interactive graphical chatbot interface.

---

## ✨ Features

- 🏥 MediCare Hospital FAQ Assistant
- 🤖 AI-based FAQ question matching
- 🧠 Natural Language Processing using NLTK
- 📊 TF-IDF text vectorization
- 🔎 Cosine Similarity matching
- 💬 Interactive Tkinter chatbot interface
- ⚡ Quick question buttons
- ⌨️ Enter key support for sending questions
- 🧹 Clear chat functionality
- 🟢 Online status indicator
- 💡 Welcome message
- 🔄 Similarity threshold for handling unknown questions
- 📁 FAQ data stored separately in JSON format

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| NLTK | Natural Language Processing and tokenization |
| Scikit-learn | TF-IDF vectorization and Cosine Similarity |
| Tkinter | Graphical User Interface |
| JSON | FAQ dataset storage |
| Regular Expressions | Text cleaning and preprocessing |

---

## 🧠 How the Chatbot Works

The chatbot follows these steps:

1. The user enters a question.
2. The question is converted to lowercase.
3. Unnecessary special characters are removed.
4. NLTK tokenizes the text.
5. FAQ questions are preprocessed in the same way.
6. TF-IDF converts the FAQ questions into numerical vectors.
7. The user's question is converted into a TF-IDF vector.
8. Cosine Similarity compares the user's question with all FAQ questions.
9. The FAQ with the highest similarity score is selected.
10. The corresponding answer is displayed in the chatbot.
11. If the similarity score is below the defined threshold, a fallback response is displayed.

---

## 📂 Project Structure

    CodeAlpha_FAQ_Chatbot/
    │
    ├── app.py
    ├── faqs.json
    ├── README.md
    └── .gitignore

### app.py

The main Python application containing:

- FAQ data loading
- Text preprocessing
- NLTK tokenization
- TF-IDF vectorization
- Cosine Similarity calculation
- Best FAQ matching
- Chatbot response generation
- Tkinter graphical interface

### faqs.json

Contains the hospital-related FAQ questions and their corresponding answers.

The FAQ dataset covers topics including:

- Hospital opening hours
- Appointment booking
- Appointment cancellation
- Appointment rescheduling
- Hospital departments
- Emergency services
- Hospital contact information
- Payment methods
- Medical reports
- Hospital location
- Laboratory services
- ICU
- Operation theatre
- Specialist doctors
- Pediatric care
- Patient visiting
- Finding a doctor
- Diagnostic services

### .gitignore

Used to prevent unnecessary files, such as the Python virtual environment, from being uploaded to GitHub.

---

## ⚙️ Requirements

Before running the project, make sure Python is installed.

The project requires:

- Python
- NLTK
- Scikit-learn
- Tkinter

---

## 🚀 Installation and Setup

### 1. Clone the Repository

    git clone https://github.com/Haniya-Ramzan/CodeAlpha_FAQ_Chatbot.git

### 2. Open the Project Folder

    cd CodeAlpha_FAQ_Chatbot

### 3. Create a Virtual Environment

    python -m venv venv

### 4. Activate the Virtual Environment

For Windows PowerShell:

    venv\Scripts\activate

### 5. Install Required Libraries

    pip install nltk scikit-learn

### 6. Run the Chatbot

    python app.py

---

## 💬 Example Questions

### Hospital Opening Hours

User:

    What are the hospital opening hours?

Chatbot:

    MediCare Hospital is open 24 hours a day, 7 days a week.

### Appointments

User:

    How can I book an appointment?

Chatbot:

    You can book an appointment by contacting the hospital reception or using the online appointment system.

### Emergency Services

User:

    Does the hospital have an emergency department?

Chatbot:

    Yes. MediCare Hospital provides emergency medical services 24 hours a day.

### ICU

User:

    Does the hospital have an ICU?

Chatbot:

    Yes. The hospital has an Intensive Care Unit for patients who require critical care and continuous monitoring.

---

## 🔍 NLP and Text Preprocessing

The chatbot uses NLTK to preprocess the questions before performing similarity matching.

The preprocessing process includes:

1. Converting text to lowercase.
2. Removing unnecessary special characters.
3. Tokenizing the text using NLTK.
4. Joining the processed tokens for further analysis.

This allows the chatbot to process the user's question and FAQ questions consistently before similarity calculation.

---

## 📊 TF-IDF Vectorization

The chatbot uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical vectors.

TF-IDF helps represent the importance of words within the FAQ questions and provides numerical representations that can be compared mathematically.

---

## 🔎 Cosine Similarity

After converting the FAQ questions and the user's question into TF-IDF vectors, the chatbot calculates their similarity using Cosine Similarity.

The chatbot identifies the FAQ with the highest similarity score and returns its corresponding answer.

This allows the system to match questions based on textual similarity rather than relying only on exact wording.

---

## 🛡️ Similarity Threshold

The chatbot uses a minimum similarity threshold to avoid returning an unrelated answer when the user's question does not sufficiently match the available FAQs.

If the similarity score is below the defined threshold, the chatbot provides a fallback response asking the user to contact the hospital reception for further assistance.

---

## 🖥️ Graphical User Interface

The chatbot includes a graphical user interface developed using Tkinter.

The interface provides:

- MediCare Hospital branding
- AI assistant title
- Online status indicator
- Chat conversation area
- User messages
- Assistant responses
- Question input field
- Send button
- Quick question buttons
- Clear chat button
- Enter key support
- Welcome message

The GUI allows users to interact with the FAQ chatbot without using the command line.

---

## 🧪 Testing

The chatbot was tested using multiple hospital-related questions.

The system successfully:

- Accepts questions from the user.
- Preprocesses the input.
- Calculates TF-IDF vectors.
- Calculates Cosine Similarity.
- Finds the most relevant FAQ.
- Displays the corresponding answer.
- Provides a fallback response when no suitable FAQ is found.

Example test questions include:

- What are the hospital opening hours?
- How can I book an appointment?
- Does the hospital have an emergency department?
- Does the hospital have an ICU?
- What departments are available at the hospital?
- Are specialist doctors available?
- Does the hospital provide laboratory services?
- Can I visit a patient in the hospital?

---

## 📋 FAQ Topics

The current FAQ dataset contains 20 hospital-related questions and answers covering areas such as:

- Hospital opening hours
- Appointments
- Appointment cancellation
- Appointment rescheduling
- Departments
- Emergency care
- Contact information
- Payment methods
- Medical reports
- Hospital location
- Laboratory services
- ICU
- Operation theatre
- Specialist doctors
- Pediatric care
- Patient visiting
- Finding a doctor
- Diagnostic services

---

## 🎓 CodeAlpha Internship Task

This project was developed for:

**CodeAlpha Artificial Intelligence Internship**

### Task 2 — FAQ Chatbot

The project implements:

- FAQ collection
- NLP preprocessing
- Similarity-based question matching
- TF-IDF vectorization
- Cosine Similarity
- Best matching answer retrieval
- Interactive chatbot interface

---

## 👩‍💻 Author

**Haniya Ramzan**

Artificial Intelligence Intern  
CodeAlpha

---

## 📜 License

This project was created for educational and internship purposes.
