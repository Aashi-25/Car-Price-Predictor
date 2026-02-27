from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
car = pd.read_csv('Cleaned Car.csv')

#creating entry function for our application
@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    car_models_by_company = {
        company: sorted(car[car['company'] == company]['name'].unique())
        for company in companies
    }
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        car_models_by_company=car_models_by_company,
        years=year,
        fuel_type=fuel_type
    )

if __name__ == "__main__":
    app.run(debug=True)