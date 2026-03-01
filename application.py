from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
car = pd.read_csv('Cleaned Car.csv')
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))


def get_form_context():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    car_models_by_company = {
        company: sorted(car[car['company'] == company]['name'].unique())
        for company in companies
    }
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].unique())
    return {
        'companies': companies,
        'car_models': car_models,
        'car_models_by_company': car_models_by_company,
        'years': years,
        'fuel_type': fuel_types
    }

#creating entry function for our application
@app.route('/')
def index():
    context = get_form_context()
    context.update({
        'predicted_price': None,
        'error_message': None,
        'selected_company': '',
        'selected_model': '',
        'selected_year': '',
        'selected_fuel_type': '',
        'selected_kms_driven': ''
    })
    return render_template('index.html', **context)


@app.route('/predict', methods=['POST'])
def predict():
    context = get_form_context()

    selected_company = request.form.get('company', '').strip()
    selected_model = request.form.get('car_model', '').strip()
    selected_year = request.form.get('year', '').strip()
    selected_fuel_type = request.form.get('fuel_type', '').strip()
    selected_kms_driven = request.form.get('kilo_driven', '').strip()

    context.update({
        'predicted_price': None,
        'error_message': None,
        'selected_company': selected_company,
        'selected_model': selected_model,
        'selected_year': selected_year,
        'selected_fuel_type': selected_fuel_type,
        'selected_kms_driven': selected_kms_driven
    })

    try:
        if not all([selected_company, selected_model, selected_year, selected_fuel_type, selected_kms_driven]):
            raise ValueError('Please fill all fields before prediction.')

        input_df = pd.DataFrame(
            [[selected_model, selected_company, int(selected_year), int(selected_kms_driven), selected_fuel_type]],
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
        )

        predicted_price = model.predict(input_df)[0]
        context['predicted_price'] = round(float(predicted_price), 2)
    except Exception as error:
        context['error_message'] = f'Prediction failed: {error}'

    return render_template('index.html', **context)

if __name__ == "__main__":
    app.run(debug=True)