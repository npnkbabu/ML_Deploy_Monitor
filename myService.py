from flask import Flask, render_template, jsonify,request
import pickle
import numpy as np

with open('height_weight.pkl','rb') as pi:
    model = pickle.load(pi)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET', 'POST'])
def temp():
    data = request.query_string
    print(data)
    my_test =np.array(float(data)).reshape(-1,1)
    ret = model.predict(my_test)
    return str(ret[0])


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)