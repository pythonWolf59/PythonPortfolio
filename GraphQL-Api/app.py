# app.py
from flask import Flask
from flask_graphql import GraphQLView
from employee_schema import schema
from employee_model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
