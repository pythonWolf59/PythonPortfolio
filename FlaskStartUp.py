from flask import Flask

app = Flask(__name__)

#Mention routes of URL's by using this decorator
@app.route('/')
#Define function for this URL
def greetUser():
    return "Welcome! You are connected to Flask Server"


#Run Local Server
if(__name__ == '__main__'):
    app.run(debug=True, use_reloader=True)
