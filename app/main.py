from flask import Flask
app = Flask(__name__)

@app.route('/question')
def hello_world():
    return [
  {
  "id": "1",
  "qcategory": "maths",
  "question": "whjhdkf ghfksh hgkshkfhdk jhvfsk",
  "correctoption": "A",
  "options":["hello","hai"]
},
  {
    "id": "2",
    "qcategory": "physics",
    "question": "df jhf hlk rerw",
    "correctoption": "B",
    "options":["hello","hai"]
  }
  ]
