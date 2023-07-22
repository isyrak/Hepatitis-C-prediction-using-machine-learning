import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder="Template")

model = pickle.load(open('C:/Users/Isyrak/Desktop/FYP PROJECT/Classifier/rfmodel','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict' , methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)

    output = round(prediction[0], 2)
    if(output == 0):
        return render_template('index.html', prediction_text ='No Hepatitis C detected')
    elif(output == 1):
        return render_template('index.html', prediction_text ='You are a normal but suspected with Hepatitis, please consult your doctor for early treatment')
    elif(output == 2):
        return render_template('index.html', prediction_text ='You are diagnosed with Hepatitis. Please consult your doctor for treatment')
    elif(output == 3):
        return render_template('index.html', prediction_text ='You are diagnosed with Fibrosis. Please consult your doctor for treatment ')
    else:
        return render_template('index.html', prediction_text ='You are diagnosed with Cirrhosis. Please consult your doctor for treatment')

if __name__ == '__main__':
    app.debug = True
    app.run()