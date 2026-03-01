# 🚢 Titanic Explorer Chatbot

An interactive full-stack data analysis chatbot built using **FastAPI** and **Streamlit**.  
This application allows users to ask natural language questions about the Titanic passenger dataset and receive both statistical insights and visualizations.

---

## 📌 Project Overview

Titanic Explorer is a data-driven chatbot that analyzes historical passenger data from the Titanic dataset.

Users can:
- Ask questions in natural language
- Receive real-time statistical responses
- View data visualizations such as histograms

The project demonstrates backend API development, frontend UI design, and data analysis integration in a complete full-stack architecture.

---

## 🏗️ Architecture

Frontend → Streamlit  
Backend → FastAPI  
Data Processing → Pandas  
Visualization → Matplotlib  

```
User
  ↓
Streamlit UI
  ↓
FastAPI Backend
  ↓
Pandas Data Processing
  ↓
Response + Visualization
```

---

## ⚙️ Tech Stack

- Python  
- FastAPI  
- Streamlit  
- Pandas  
- Matplotlib  
- Requests  

---

## 📂 Project Structure

```
titanic-chatbot/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── titanic.csv
│
├── frontend/
│   ├── app.py
│
├── requirements.txt
└── README.md
```
---
 ## Website Link 

https://titanic-chatbot-afvuqycktmbcrfvxyha57p.streamlit.app/

---

## ✨ Features

- Natural language question processing  
- Passenger demographic analysis  
- Ticket fare statistics  
- Embarkation port breakdown  
- Age distribution histogram visualization  
- Clean and styled Streamlit UI  
- API-based backend architecture  

---

## 🧪 Example Questions

- What percentage of passengers were male?  
- What was the average ticket fare?  
- Where did passengers embark from?  
- Show age histogram  

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/titanic-chatbot.git
cd titanic-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend (FastAPI)

Navigate to backend folder:

```bash
cd backend
```

Run:

```bash
uvicorn main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

---

### 5️⃣ Run Frontend (Streamlit)

Open a new terminal.

Navigate to frontend folder:

```bash
cd frontend
```

Run:

```bash
streamlit run app.py
```

Application will open at:

```
http://localhost:8501
```

---

## 📊 Dataset

The application uses the Titanic dataset containing passenger information such as:

- Passenger class  
- Gender  
- Age  
- Ticket fare  
- Embarkation port  

This dataset is commonly used for data analysis and machine learning tasks.

---

## 🔍 API Endpoint

### POST `/ask`

Request Body:

```json
{
  "question": "What percentage of passengers were male?"
}
```

Response:

```json
{
  "answer": "64.76% of passengers were male.",
  "image": "<base64_string_if_applicable>"
}
```

---

## 📈 Visualization Handling

When a visualization is requested (e.g., age histogram):

- Backend generates plot using Matplotlib  
- Image is encoded in Base64  
- Frontend decodes and renders image dynamically  

---

## 🧠 Learning Outcomes

This project demonstrates:

- Building REST APIs with FastAPI  
- Creating interactive UIs with Streamlit  
- Processing real-world datasets with Pandas  
- Implementing visualization pipelines  
- Integrating frontend and backend systems  

---

## 📌 Future Improvements

- Replace rule-based query logic with advanced NLP processing  
- Add more dynamic visualization types  
- Deploy backend on a cloud platform  
- Deploy frontend on Streamlit Cloud  
- Add chat history and session memory  

---

## 📜 License

This project is intended for educational and portfolio purposes.
