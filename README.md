<div align="center">

# 🐍 Python Requests Module

### Exploring the World of HTTP Requests & API Communication

A hands-on Python learning repository dedicated to understanding the Requests library and how Python communicates with web servers and APIs.

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Library](https://img.shields.io/badge/Library-Requests-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Learning-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📌 About This Repository

Welcome to my **Python Requests Module** repository!

This is one of my first steps toward understanding how Python interacts with the internet.

The main purpose of this repository is to explore the Python `requests` library, understand HTTP communication, and learn how to interact with web APIs.

Instead of just learning theory, I'm focusing on practical implementation and experimenting with different functionalities.

### 🎯 Learning Objectives

- Understand the Python Requests library.
- Learn how HTTP requests work.
- Explore GET and POST methods.
- Understand API communication.
- Work with JSON responses.
- Handle HTTP errors and exceptions.
- Develop practical Python programming skills.

---

## 🧠 What is the Requests Module?

The `requests` library is a popular Python library used to send HTTP requests and communicate with web servers.

It allows Python programs to:

- Retrieve information from websites.
- Send data to APIs.
- Download online resources.
- Work with JSON responses.
- Communicate with external services.

**In simple words:** Requests allows Python to communicate with the internet.

---

## ⚙️ Installation

Before using the Requests library, install it using pip.

```bash
pip install requests
```

Import the library into your Python program:

```python
import requests
```

---

## 💻 Practical Examples

### 1. GET Request

Used to retrieve information from a server.

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)
print(response.text)
```

### 2. Checking Website Status

```python
import requests

url = "https://www.python.org"

response = requests.get(url)

if response.status_code == 200:
    print("Website is working!")
else:
    print("Something went wrong!")
```

### 3. Working with JSON

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data)
```

### 4. Handling Exceptions

```python
import requests

try:
    response = requests.get(
        "https://api.github.com",
        timeout=10
    )

    response.raise_for_status()

    print(response.status_code)

except requests.exceptions.RequestException as error:
    print("Error:", error)
```

---

## 📚 Important Concepts

| Concept | Description |
|---|---|
| `requests.get()` | Retrieves information |
| `requests.post()` | Sends data to a server |
| `requests.put()` | Updates existing resources |
| `requests.delete()` | Deletes resources |
| `response.status_code` | Returns HTTP status code |
| `response.text` | Returns response as text |
| `response.json()` | Converts JSON response into Python data |
| `response.headers` | Provides response headers |
| `response.url` | Returns the final response URL |

---

## 🌐 Understanding HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 301 | Moved Permanently |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 📂 Repository Structure

```text
Requests-Module/
│
├── README.md
│
└── main.py
```

| File | Purpose |
|---|---|
| `README.md` | Documentation and learning reference |
| `main.py` | Python practice and implementation |

---

## 🚀 My Learning Journey

This repository represents my journey of learning Python and exploring its libraries.

I'm currently building my programming foundations and gradually moving toward more advanced concepts in:

- Python Programming
- Data Science
- Machine Learning
- Artificial Intelligence
- API Development

Every repository is another step toward becoming a better developer.

---

## 🔮 What's Next?

- [ ] Explore GET and POST requests.
- [ ] Understand HTTP headers.
- [ ] Learn query parameters.
- [ ] Work with JSON APIs.
- [ ] Explore API authentication.
- [ ] Practice exception handling.
- [ ] Build small projects using Requests.

---

## 👨‍💻 About Me

**Aryan Jain**

B.Tech | Computer Science Engineering (AI & ML)

I'm passionate about Python, Artificial Intelligence, Machine Learning, and exploring how technology works behind the scenes.

Currently learning, experimenting, and building projects one step at a time.

### Let's Connect!

[![GitHub](https://img.shields.io/badge/GitHub-Aryanbhayji-black?style=for-the-badge&logo=github)](https://github.com/Aryanbhayji)

---

<div align="center">

### ⭐ If you find this repository useful, feel free to explore it!

**Learning Today. Building Tomorrow. 🚀**

</div>
