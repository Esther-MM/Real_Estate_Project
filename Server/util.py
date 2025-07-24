import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__model = None
__column_data = None

def get_estimated_price(location, total_sqft, bedrooms, bath):
    try:
        index_location = __column_data.index(location.lower())
    except:
        index_location = -1

    x = np.zeros(len(__column_data))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bedrooms

    if index_location >= 0:
        x[index_location] = 1


    return round(__model.predict([x])[0], 2)
    # x_df = pd.DataFrame([x], columns=__column_data)
    # return round(__model.predict(x_df)[0], 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...Start")
    global __locations
    global __column_data

    with open("./artifacts/models_columns.json", 'r') as f:
        __column_data = json.load(f)['column_data']
        __locations = __column_data[3:]

    global __model
    with open("./artifacts/Price_Prediction_Model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...Done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Indira Nagar', 1000, 2, 2))
    print(get_estimated_price('Indira Nagar', 1000, 3, 3))
