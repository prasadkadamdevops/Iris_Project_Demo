from flask import Flask, render_template, jsonify, request
import pandas as pd
from utils import Iris
import config

app = Flask(__name__)


@app.route('/')
def flask():
    print("Welcome to Flask")
    return "Hello"


@app.route('/test3')
def test3():
    return render_template('home.html')


@app.route('/species', methods=['POST'])  # Ensure this route accepts POST requests
def get_predict_species():
    data = request.form
    print("Data is:", data)

    try:
        # Retrieve input values from the request data
        SepalLengthCm = float(data['SepalLengthCm'])
        SepalWidthCm = float(data['SepalWidthCm'])
        PetalLengthCm = float(data['PetalLengthCm'])
        PetalWidthCm = float(data['PetalWidthCm'])

        # Create an instance of the Iris class
        ir = Iris(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

        # Get the predicted species
        species = ir.get_predict_species()

        return jsonify({'Result': f"Predicted species is: {species}"})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'Error': 'An error occurred during prediction.'}), 500


if __name__ == '__main__':
    app.run(port=config.PORT_NUMBER, debug=False)
