from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)

heart_model = pickle.load(open('heart_model.pkl', 'rb'))
ordinal_e = pickle.load(open('oe.pkl', 'rb'))
min_max = pickle.load(open('mm.pkl', 'rb'))

columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak','ST_Slope']

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        the_request = request.form.to_dict()
        request_df = pd.DataFrame([the_request])        

        cat_variables = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']      
        mm_variables = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        
        request_df[cat_variables] = ordinal_e.transform(request_df[cat_variables])
        request_df[mm_variables] = min_max.transform(request_df[mm_variables])
                    
        result = heart_model.predict(request_df)
        print(result)
        
        if result[0] == 1:
            return render_template('result.html', prediction_text='You have a heart disease')
        else:
            return render_template('result.html', prediction_text='You do not have a heart disease')
                
    return render_template('index.html')


    

if __name__ == '__main__':
    app.run(debug=True)

