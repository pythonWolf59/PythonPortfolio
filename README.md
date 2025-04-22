# 🐍 Flask API Playground

Welcome to my Flask repository!

This project is a personal backend playground where I build and experiment with **Flask APIs**, CRUD operations, and backend integration using modern Python tools. It's aimed at learning, practicing, and eventually deploying scalable backend services.

---

## 🔧 What’s Inside?

- ✅ Flask project structure using **Blueprints**
- ✅ CRUD APIs (Create, Read, Update, Delete)
- ✅ SQLAlchemy ORM with **SQLite** database
- ✅ Integration with **Gradio** for simple UI testing
- ✅ RESTful routes for backend operations

---

## 📁 Project Structure

```
BasicFlaskCRUD/
│
├── .gitignore              # Files and folders to exclude from Git tracking (e.g. __pycache__, .env)
├── README.md               # Project overview and documentation
├── requirements.txt        # List of Python packages to install
│
├── database.py             # SQLAlchemy database engine and session setup
├── models.py               # SQLAlchemy models (e.g. User model)
├── routes.py               # API routes using Flask Blueprints (CRUD operations)
├── FlaskStartUp.py         # Main app entry point (Flask app, server setup)
├── gradio_ui.py            # Gradio frontend interface for testing APIs
│
└── __pycache__/            # Compiled Python files (auto-generated, ignored by Git)


---

## 🧪 How to Run

1. **Clone this repo**  
   ```bash
   git clone https://github.com/pythonWolf59/PythonPortfolio.git
   git switch Flask-Apps
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**  
   ```bash
   python BasicFlaskCRUD\FlaskStartUp.py
   ```

5. **Launch the Gradio UI (Optional)**  
   ```bash
   python BasicFlaskCRUD\gradio_ui.py
   ```

---

## 🚀 Roadmap

- [x] CRUD APIs using Blueprints  
- [x] Gradio UI for testing endpoints  
- [ ] Add authentication (JWT or session-based)  
- [ ] Add PostgreSQL & deploy on Render/Vercel  
- [ ] Create reusable API templates  
- [ ] Build microservices with FastAPI or Flask  

---

## 🤝 Contributions

This is a personal learning project, but feel free to fork it and build your own version. PRs and issues are welcome if you want to collaborate or suggest improvements.

---

## 📢 Contact

If you’d like to connect or have questions, feel free to reach out:

- LinkedIn: https://www.linkedin.com/in/hamza-sareer-7515a0170/
- Email: humxazakir11@gmail.com

---

**Happy coding! 🚀**

