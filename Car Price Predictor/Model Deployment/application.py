# flask, pandas, scikit-learn, pickle-mixin
from flask import Flask
from flask import render_template
import pandas as pd


app=Flask(__name__)
cars = pd.read_csv("cleaned_cars_data.csv")


@app.route('/')
def index():
    companies = sorted(cars['company'].unique())
    car_models = sorted(cars['name'].unique())
    year = sorted(cars['year'].unique(), reverse=True)
    fuel_type = sorted(cars['fuel_type'].unique())
    return render_template('index.html',companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)

if __name__ == "__main__":
    app.run(debug=True)
