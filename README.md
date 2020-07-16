# question-service

## Install the dependencies.

Make sure you have Python 3 and Pip 3 installed.

```
pip3 install -r requirements.txt
```

Once the dependencies are installed, run the server.

```
export FLASK_APP=hello.py
flask run
```

Access the API

```
curl http://127.0.0.1:5000/question
```