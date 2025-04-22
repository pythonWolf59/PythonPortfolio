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
.
├── app/
│   ├── __init__.py          # Flask app setup
│   ├── routes.py            # All API endpoints
│   ├── models.py            # SQLAlchemy models
│   └── database.py          # DB connection/session setup
├── gradio_ui.py             # Gradio interface for API testing
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🧪 How to Run

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/flask-api-playground.git
   cd flask-api-playground
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
   python app/main.py
   ```

5. **Launch the Gradio UI (Optional)**  
   ```bash
   python gradio_ui.py
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

