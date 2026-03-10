import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/bengaluru_house_prices.csv")

df = df.drop(['area_type','availability','society'], axis=1)
df = df.dropna()

df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))
df = df.drop(['size'], axis=1)

def convert_sqft(x):
    tokens = str(x).split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df = df.dropna()

location_stats = df['location'].value_counts()
locations_less_than_10 = location_stats[location_stats <= 10]

df['location'] = df['location'].apply(
    lambda x: 'other' if x in locations_less_than_10 else x
)

df = pd.get_dummies(df, columns=['location'])

X = df.drop(['price'], axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model/house_model.pkl")
joblib.dump(X.columns, "model/model_columns.pkl")

print("Model trained successfully")