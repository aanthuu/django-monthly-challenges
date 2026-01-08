# 📅 Monthly Challenges Web App

Hi! This is my very first **Django Project**. 

I built this web application to learn how the backend of a website works using Python. The app helps users see a specific "Challenge" for every month of the year (like "Read a book" in January or "Go to the gym" in February).

## 🚀 About the Project

As a fresher learning Python Backend Development, I wanted to move beyond basic Python scripts and build a real web application. 

This project doesn't use a database yet (I'm learning that next!). Instead, it focuses heavily on **URL Routing** and **Views logic** to handle user requests dynamically.

<img width="1893" height="856" alt="Screenshot 2026-01-08 113828" src="https://github.com/user-attachments/assets/b4f36580-80e8-4021-b667-41df95627ebd" />
<img width="1885" height="825" alt="Screenshot 2026-01-08 113858" src="https://github.com/user-attachments/assets/bf79a6f7-7fdc-4fd3-9605-1c4723ea180e" />

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Django 5.x
* **Frontend:** HTML5 & Django Templates (DTL)
* **Styling:** Basic CSS

## ✨ Key Features

1.  **Dynamic URLs:** You can type `/challenges/january` or `/challenges/december`, and the page updates automatically without me creating 12 separate HTML files.
2.  **Smart Redirects:** If you type a number like `/challenges/1`, it automatically redirects you to `/challenges/january`.
3.  **Dynamic Navigation:** The links on the homepage are generated using Python loops, so they never break.
4.  **Error Handling:** If you try to visit a month that doesn't exist (like `/challenges/octember`), it shows a custom "404 Not Found" message.

## 🧠 What I Learned

Building this helped me understand the "MVT" (Model-View-Template) architecture of Django. Here are the specific concepts I practiced:
* **Routing:** How to use `urls.py` to capture variables (integers and strings) from the browser address bar.
* **Views:** Writing Python functions to process data and send responses.
* **Templates:** Using Jinja-like syntax (`{% for %}`, `{% if %}`) to inject Python data into HTML.
* **Reverse Resolution:** Using the `reverse()` function to generate URLs dynamically instead of hardcoding them.

## 💻 How to Run This Project

If you want to try this on your machine:

1.  **Clone the repository** (or download the folder):
    ```bash
    git clone <your-repo-link-here>
    ```

2.  **Install Django:**
    ```bash
    pip install django
    ```

3.  **Run the Server:**
    Open your terminal in the project folder and type:
    ```bash
    python manage.py runserver
    ```

4.  **Visit the App:**
    Open your browser and go to: `http://127.0.0.1:8000/challenges/`

## 🔮 Future Improvements

Right now, the data is stored in a Python Dictionary. In the future, I plan to:
* Connect this to a **Database** (SQLite/PostgreSQL) so users can add their own challenges.
* Add a **User Login** system so everyone can have their own private list.
* Improve the **CSS/Design** to make it look modern.

---
*Created by Ananthu Krishnan as part of my journey to becoming a Python Backend Developer.*
