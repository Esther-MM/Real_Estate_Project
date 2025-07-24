from flask import Flask, request, jsonify
# from future.backports.http.client import responses

import util

app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return "Hi"

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_real_estate_price', methods = ['POST'])
def predict_real_estate_price():
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bedrooms = int(request.form['bedrooms'])
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bedrooms, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Real Estate Price Prediction...")
    util.load_saved_artifacts()
    app.run()