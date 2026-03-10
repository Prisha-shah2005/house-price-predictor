import joblib
import numpy as np

model = joblib.load("model/house_model.pkl")
columns = joblib.load("model/model_columns.pkl")

def predict_price(location, sqft, bath, bhk):

    x = np.zeros(len(columns))

    x[columns.get_loc("total_sqft")] = sqft
    x[columns.get_loc("bath")] = bath
    x[columns.get_loc("bhk")] = bhk

    location_column = "location_" + location

    if location_column in columns:
        x[columns.get_loc(location_column)] = 1

    price = model.predict([x])[0]

    return round(price,2)