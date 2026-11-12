# Day 01 - Environment Setup & Hello AI

## Objective

Welcome to Day 01 of the 21-Day AI Assistant Learning Journey.

Today, we will prepare our development environment and run our first AI application locally using Ollama and a Large Language Model (LLM).

By the end of this session, you will be able to:

- Install Python
- Install Visual Studio Code
- Install Ollama
- Download an AI model
- Create a Python virtual environment
- Configure your project
- Write your first AI program
- Receive a response from a local AI model

---

# 📖 What We Will Build Today

We will create a simple Python application that asks an AI model a question and displays the response.

Example:

**Question**

```text
What is Artificial Intelligence?
```

**Output**

```text
Artificial Intelligence (AI) is a branch of computer science that enables computers to perform tasks that typically require human intelligence.
```

---

# Step 1: Install Python

Python is one of the most popular programming languages for Artificial Intelligence, Machine Learning, Automation, and Data Science.

### Verify Python Installation

Open a terminal or command prompt and run:

```bash
python --version
```

or

```bash
python3 --version
```

Expected output:

```bash
Python 3.12.5
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

# Step 2: Install Visual Studio Code

Download:

https://code.visualstudio.com/download

---

# Step 3: Install Ollama

Download:

https://ollama.com/download

Verify:

```bash
ollama --version
```

---

# Step 4: Download Your First AI Model

```bash
ollama pull qwen3:1.7b
```

Optional:

```bash
ollama pull qwen3:4b
```

---

# Step 5: Verify Ollama Is Working

```bash
ollama run qwen3:1.7b
```

---

# Step 6: Create the Project Folder

```text
AI-Assistant-Learning/
│
├── Day_01/
│
└── README.md
```

---

# Step 7: Open the Project in VS Code

File → Open Folder

---

# Step 8: Create a Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

---

# Step 9: Install Required Libraries

```bash
pip install openai python-dotenv

pip freeze > requirements.txt
```

---

# Step 10: Create the Environment Configuration File

Create `.env`

```env
BASE_URL=http://localhost:11434/v1
API_KEY=ollama
MODEL=qwen3:1.7b
```

---

# Step 11: Create Your First AI Program

Create `hello_ai.py`

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence?"
        }
    ]
)

print(response.choices[0].message.content)
```

---

# Step 12: Run the Program

```bash
python hello_ai.py
```

---

# ✅ Day 01 Summary

Today you learned:

- Python Installation
- VS Code Setup
- Ollama Installation
- Downloading AI Models
- Virtual Environments
- Environment Variables
- Connecting Python with Ollama
- Running Your First AI Program

---

