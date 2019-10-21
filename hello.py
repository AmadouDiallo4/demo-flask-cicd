"""ecrire ici un projet""" 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """ Affiche Hello"""
    return "Hello Gens de Fitec-Faurecia!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
