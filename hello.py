"""test"""

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def index():
    """Affiche Hello"""

    return '''
<!doctype html>
<html>
<head>
    <title> Ceci est mon site </title>
</head>

<body> 
    <p><h1> Hello World!'</h1></p>
    <p><h2> Gurs Fitec Faurecia </h2></p>
</body>
'''

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
