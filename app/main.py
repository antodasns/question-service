from flask import Flask
app = Flask(__name__)

@app.route('/question')
def hello_world():
    return {
        "question_description": "",
        "options": ['A', 'B', 'C', 'D']
    }