from flask import Blueprint, request, jsonify
from database import SessionLocal
from models import User

api = Blueprint('api', __name__)
session = SessionLocal()

# CREATE
@api.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    if session.query(User).filter_by(email=data["email"]).first():
        return jsonify({"error": "User with this email already exists!"}), 400
    
    new_user = User(
        username=data["username"],
        email=data["email"],
        full_name=data["full_name"],
        hashed_password=data["hashed_password"]
    )
    session.add(new_user)
    session.commit()
    return jsonify({"message": "User created successfully!"}), 201

# READ BY EMAIL
@api.route('/read_by_email/<email>', methods=['GET'])
def read_user_by_email(email):
    user = session.query(User).filter_by(email=email).first()
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name
        })
    return jsonify({"error": "User not found"}), 404

# UPDATE BY EMAIL
@api.route('/update_by_email/<email>', methods=['PUT'])
def update_user_by_email(email):
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if "username" in data and data["username"]:
        user.username = data["username"]
    if "full_name" in data and data["full_name"]:
        user.full_name = data["full_name"]
    if "hashed_password" in data and data["hashed_password"]:
        user.hashed_password = data["hashed_password"]

    session.commit()
    return jsonify({
        "message": "User updated",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name
        }
    })

# DELETE BY EMAIL
@api.route('/delete_by_email/<email>', methods=['DELETE'])
def delete_user_by_email(email):
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    session.delete(user)
    session.commit()
    return jsonify({
        "message": "User deleted",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    })
