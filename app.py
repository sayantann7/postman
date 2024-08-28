from flask import Flask, request
app = Flask(__name__)

stored_age = 26

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/sit')
def sit():
    return "SIT ROCKS!"

@app.route('/sheela')
def sheela():
    return f"Sheela ki jawani! Umar {stored_age}"

@app.route('/sheela/<age>')
def sheela_age(age):
    return f"Sheela ki umar {age}."

@app.route('/sheela', methods=['POST'])
def sheela_post():
    global stored_age
    age = request.form.get('age')
    stored_age = age
    return "Done!"

app.run()
