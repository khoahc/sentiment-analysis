import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import gzip
from predict import model_fn
from predict import predict_fn
from utils import review_to_words
from utils import convert_and_pad
app = Flask(__name__)
model = model_fn('models\\vi')

print(model)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    result =''
    review_input = request.form['text'].encode('utf-8')
    # input_data_words = review_to_words(review_input)
    # data_X, data_len = convert_and_pad(model.word_dict, input_data_words)
    print(review_input)
    predict = predict_fn(review_input, model)
    if predict == 1:
        result = 'Tich cuc'
    else:
        result = 'Tieu cuc'

    return render_template('index.html', prediction_text='Ket qua $ {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)