from flask import Flask, request, render_template, jsonify
from predict import model_fn
from predict import predict_fn
from flask import Flask, request, render_template

from predict import model_fn
from predict import predict_fn

app = Flask(__name__)
model = model_fn('models/vi')

print(model)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    result = {}
    review_input = request.form['text'].encode('utf-8')
    if len(review_input) > 0:
        # input_data_words = review_to_words(review_input)
        # data_X, data_len = convert_and_pad(model.word_dict, input_data_words)
        predict, percent = predict_fn(review_input, model)
        # print(predict, float(percent))
        if predict == 1:
            result['code'] = 1
            result['msg'] = 'Tích cực'
        else:
            result['code'] = 0
            result['msg'] = 'Tiêu cực'
        result['percent'] = float(percent)

        print(request.form['text'].strip() + " --> " + result.get('msg'))
    else:
        result['code'] = -1
        result['msg'] = 'Bạn chưa nhập review'

    return jsonify(result)
    # return render_template('index.html', prediction_text='Kết quả: {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)