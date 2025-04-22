import gradio as gr
import requests

BASE_URL = "http://127.0.0.1:5500"

def create_user(username, email, full_name, password):
    response = requests.post(f"{BASE_URL}/create", json={
        "username": username,
        "email": email,
        "full_name": full_name,
        "hashed_password": password
    })
    return response.json()

def read_user(email):
    response = requests.get(f"{BASE_URL}/read_by_email/{email}")
    return response.json()

def update_user(email, username, full_name, password):
    response = requests.put(f"{BASE_URL}/update_by_email/{email}", json={
        "username": username or None,
        "full_name": full_name or None,
        "hashed_password": password or None
    })
    return response.json()

def delete_user(email):
    response = requests.delete(f"{BASE_URL}/delete_by_email/{email}")
    return response.json()

with gr.Blocks() as demo:
    gr.Markdown("## 🔧 User Management Panel (CRUD)")

    with gr.Tab("Create User"):
        username = gr.Textbox(label="Username")
        email = gr.Textbox(label="Email")
        full_name = gr.Textbox(label="Full Name")
        password = gr.Textbox(label="Password", type="password")
        create_btn = gr.Button("Create")
        create_output = gr.JSON()
        create_btn.click(fn=create_user, inputs=[username, email, full_name, password], outputs=create_output)

    with gr.Tab("Read User"):
        read_email = gr.Textbox(label="User Email")
        read_btn = gr.Button("Read")
        read_output = gr.JSON()
        read_btn.click(fn=read_user, inputs=[read_email], outputs=read_output)

    with gr.Tab("Update User"):
        upd_email = gr.Textbox(label="User Email")
        upd_username = gr.Textbox(label="New Username (optional)")
        upd_full_name = gr.Textbox(label="New Full Name (optional)")
        upd_password = gr.Textbox(label="New Password (optional)", type="password")
        update_btn = gr.Button("Update")
        update_output = gr.JSON()
        update_btn.click(fn=update_user, inputs=[upd_email, upd_username, upd_full_name, upd_password], outputs=update_output)

    with gr.Tab("Delete User"):
        del_email = gr.Textbox(label="User Email")
        delete_btn = gr.Button("Delete")
        delete_output = gr.JSON()
        delete_btn.click(fn=delete_user, inputs=[del_email], outputs=delete_output)

demo.launch()