from flask import Flask
from livereload import Server
from database import Base, engine
from routes import api  # Import the blueprint

app = Flask(__name__)
app.register_blueprint(api)  # Register the blueprint

# Create tables
Base.metadata.create_all(bind=engine)

@app.route('/')
def greet_user():
    return "Default Page - write route name after / in the URL to access other routes!"

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(debug=True)

