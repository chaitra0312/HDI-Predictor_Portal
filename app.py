from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load your pre-trained model matrix safely
model_path = os.path.join('models', 'hdi_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def get_hdi_tier(score):
    if score >= 0.800: return "Very High Human Development"
    elif score >= 0.700: return "High Human Development"
    elif score >= 0.550: return "Medium Human Development"
    else: return "Low Human Development"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve features from HTML form inputs
    input_features = [float(x) for x in request.form.values()]
    final_features = [np.array(input_features)]
    
    # Predict and bound the score realistically between 0.0 and 1.0
    prediction = model.predict(final_features)[0]
    predicted_score = max(0.0, min(1.0, prediction))
    
    # Categorize into development tier
    tier = get_hdi_tier(predicted_score)
    
    return render_template('index.html', 
                           prediction_text=f'Predicted HDI Score: {predicted_score:.4f}',
                           tier_text=tier)

if __name__ == "__main__":
    app.run(debug=True)