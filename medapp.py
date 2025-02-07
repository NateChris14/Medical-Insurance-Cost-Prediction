from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd  # Import Pandas to maintain feature names

# Load model and preprocessors
med_model = pickle.load(open('med_model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Getting user input from form
        data = request.form

        # Create a dictionary for input features
        input_data = {
            'age': [float(data['age'])],
            'sex': [data['sex'].strip().lower()],
            'bmi': [float(data['bmi'])],
            'children': [int(data['children'])],
            'smoker': [data['smoker'].strip().lower()],
            'region': [data['region'].strip().lower()]
        }

        # Convert input into a Pandas DataFrame (to match training data format)
        input_df = pd.DataFrame(input_data)

        # Encode categorical features (handling unexpected values)
        try:
            encoded_values = encoder.transform(input_df[['sex', 'smoker']])  # Pass as DataFrame
            input_df[['sex', 'smoker']] = encoded_values  # Replace with encoded values
        except Exception as e:
            return jsonify({'error': f'Encoding failed. Check `sex` and `smoker` values. Error: {str(e)}'})

        # One-Hot Encode `region`
        region_encoded = pd.get_dummies(input_df['region'], drop_first=True)  # Automatically encodes
        expected_regions = ['northwest', 'southeast', 'southwest']  # Expected features from training
        for col in expected_regions:  # Ensure all expected columns exist
            if col not in region_encoded:
                region_encoded[col] = 0
        input_df = input_df.drop(columns=['region']).join(region_encoded)

        # Ensure the column order matches the training data
        feature_order = ['age', 'sex', 'bmi', 'children', 'smoker', 'northwest', 'southeast', 'southwest']
        input_df = input_df[feature_order]  # Reorder columns

        # Apply scaling to numeric features
        try:
            input_df[['age', 'bmi', 'children']] = scaler.transform(input_df[['age', 'bmi', 'children']])
        except Exception as e:
            return jsonify({'error': f'Scaling failed. Error: {str(e)}'})

        # Make prediction (log-transformed)
        prediction_log = med_model.predict(input_df)  # Pass as DataFrame
        prediction = np.expm1(prediction_log)  # Convert back from log scale

        # Return prediction result
        return jsonify({'Predicted Charges': round(float(prediction[0]), 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
