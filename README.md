# 🚢 Titanic Explorer Chatbot

An interactive full-stack data analysis chatbot built using **FastAPI** and **Streamlit**.  
This application allows users to ask natural language questions about the Titanic passenger dataset and receive both statistical insights and visualizations.

---

## 🌐 Live Demo

👉 **Try it now:** [https://titanic-chatbot-afvuqycktmbcrfvxyha57p.streamlit.app/](https://titanic-chatbot-afvuqycktmbcrfvxyha57p.streamlit.app/)

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

```
User
  ↓
Streamlit UI  (frontend/app.py — runs on port 8501)
  ↓  HTTP POST /ask
FastAPI Backend  (backend/main.py — runs on port 8000)
  ↓
Pandas Data Processing  (backend/agent.py)
  ↓
Response + Optional Visualization (Matplotlib → base64 PNG)
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend UI | Streamlit |
| Backend API | FastAPI + Uvicorn |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| HTTP Client | Requests |
| Language | Python 3.7+ |

---

## 📂 Project Structure

```
titanic-chatbot/
│
├── backend/
│   ├── main.py        ← FastAPI server (the /ask endpoint)
│   ├── agent.py       ← Query processing logic
│   └── titanic.csv    ← Titanic passenger dataset (891 rows)
│
├── frontend/
│   └── app.py         ← Streamlit web UI
│
├── requirements.txt   ← All Python dependencies
└── README.md
```

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

You can type any of these into the chatbot:

- How many passengers were on the Titanic?
- What percentage of passengers were male?
- What percentage of passengers were female?
- How many passengers survived?
- What was the average ticket fare?
- What was the highest ticket fare?
- How many passengers were in each class?
- How many children were on board?
- What was the average age of passengers?
- Where did passengers embark from?
- Show me the age histogram

---

## 🚀 How to Run Locally — Step-by-Step (Beginner Friendly)

> **You need two terminal windows open at the same time** — one for the backend and one for the frontend.

---

### ✅ Prerequisites

Before starting, make sure you have the following installed on your computer:

#### 1. Python 3.7 or higher

- **Download:** https://www.python.org/downloads/
- During installation on Windows, **check the box "Add Python to PATH"**
- Verify installation by opening a terminal and running:

  ```bash
  python --version
  ```
  or on Mac/Linux:
  ```bash
  python3 --version
  ```
  You should see something like `Python 3.11.x`.

#### 2. pip (Python package manager)

pip is included with Python. Verify it works:

```bash
pip --version
```

#### 3. Git

- **Download:** https://git-scm.com/downloads
- Verify installation:

  ```bash
  git --version
  ```

---

### 1️⃣ Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/milindgajbhiye/titanic-chatbot.git
cd titanic-chatbot
```

---

### 2️⃣ Create a Virtual Environment

A virtual environment keeps this project's dependencies separate from other Python projects.

```bash
python -m venv .venv
```

> On Mac/Linux, use `python3` instead of `python` if the above command fails.

Now **activate** the virtual environment:

**Windows (Command Prompt / PowerShell)**
```bash
.venv\Scripts\activate
```

**Mac / Linux**
```bash
source .venv/bin/activate
```

After activation, your terminal prompt will change to show `(.venv)` at the beginning — this means the virtual environment is active.

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required packages: FastAPI, Streamlit, Pandas, Matplotlib, Requests, Pillow, and Uvicorn.  
Wait for it to finish (may take 1–2 minutes on first run).

---

### 4️⃣ Start the Backend Server (Terminal 1)

> Keep this terminal open and running while you use the app.

Navigate to the backend folder and start the API server:

```bash
cd backend
uvicorn main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

✅ The backend is now running at **http://127.0.0.1:8000**

---

### 5️⃣ Start the Frontend (Terminal 2)

> Open a **new/second terminal window**. Navigate back to the project root first.

```bash
cd titanic-chatbot      # if you opened a fresh terminal
source .venv/bin/activate   # Mac/Linux — re-activate the virtual environment
# OR on Windows:
# .venv\Scripts\activate

cd frontend
streamlit run app.py
```

You should see output like:
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

✅ Your browser should automatically open at **http://localhost:8501**

---

### 6️⃣ Use the Chatbot

1. Type a question in the input box (e.g., *"How many passengers survived?"*)
2. Click the **✨ Ask** button
3. The answer appears below

---

### ⚠️ Important Notes

| ⚠️ | Detail |
|----|--------|
| **Order matters** | Always start the **backend first** (Step 4), then the frontend (Step 5) |
| **Two terminals** | Keep both terminal windows open while using the app |
| **Virtual env** | Make sure `(.venv)` is shown in both terminals before running commands |
| **Stop servers** | Press `CTRL+C` in each terminal to stop the backend/frontend |

---

## 🛠️ Troubleshooting

### ❌ "python is not recognized" (Windows)
Reinstall Python from https://www.python.org/downloads/ and make sure to check **"Add Python to PATH"** during setup.

### ❌ "uvicorn: command not found"
The virtual environment might not be activated. Run the activate command again:
- Windows: `.venv\Scripts\activate`
- Mac/Linux: `source .venv/bin/activate`

### ❌ "Can't connect to the backend server"
The backend is not running. Go to Terminal 1 and run:
```bash
cd backend
uvicorn main:app --reload
```

### ❌ "streamlit: command not found"
Dependencies might not be installed. Run:
```bash
pip install -r requirements.txt
```

### ❌ Browser does not open automatically
Manually open your browser and go to: **http://localhost:8501**

### ❌ Port already in use
If port 8000 or 8501 is taken by another process, you can use different ports:
```bash
# Backend on a different port (e.g. 8001)
uvicorn main:app --reload --port 8001

# Frontend on a different port (e.g. 8502)
streamlit run app.py --server.port 8502
```
> If you change the backend port, update the `BACKEND_URL` constant at the top of `frontend/app.py` to match.

---

## 📊 Dataset

The application uses the Titanic dataset (`backend/titanic.csv`) containing information on 891 passengers:

| Column | Description |
|--------|-------------|
| `survived` | 0 = No, 1 = Yes |
| `pclass` | Ticket class (1st, 2nd, 3rd) |
| `sex` | male / female |
| `age` | Passenger age (some values missing) |
| `fare` | Ticket price in USD |
| `embarked` | Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

---

## 🔍 API Endpoint

### POST `/ask`

Send a question and receive an answer.

**Request Body:**
```json
{
  "question": "What percentage of passengers were male?"
}
```

**Response (text answer):**
```json
{
  "answer": "64.76% of passengers were male.\nThat is 577 out of 891 total passengers."
}
```

**Response (with visualization):**
```json
{
  "answer": "Here is the age distribution histogram.",
  "image": "<base64_encoded_PNG_string>"
}
```

You can also test the API directly in your browser at: **http://127.0.0.1:8000/docs** (interactive Swagger UI)

---

## 📈 Visualization Handling

When you ask for an age histogram:

1. Backend generates the plot using Matplotlib  
2. Image is encoded as a Base64 PNG string  
3. Frontend decodes it and renders it as an image  

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
- Add chat history and session memory  

---

## 📜 License

This project is intended for educational and portfolio purposes.
