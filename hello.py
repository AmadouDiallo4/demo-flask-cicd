""" test"""

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def index():
    """ Affiche Hello """

    return "Hello Gens de Fitec-Faurecia!"

if __name__ == "__main__":
    """ function main """
    APP.run(host="0.0.0.0", port=5000)
