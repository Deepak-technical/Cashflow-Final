from flask import Flask ,request,render_template
import pickle
import numpy as np
# from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('prediction (1).pkl','rb'))
model2=pickle.load(open('xgb_model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        month = int(request.form['month'])
        type2 = int(request.form['type'])
        cap = int(request.form['cap'])
        print(month)
        print(type2)
        print(cap)
       
        if type2==3:
            data=np.array([[month,type2,cap]])
            prediction=model2.predict(data)
        else:

            data=np.array([[month]])
            prediction=model.predict(data)

       
        print(prediction)
        return render_template ("predict.html",prediction=float(prediction[0]))

    else:
        return render_template("predict.html")


@app.route('/chat')
def chat():
    return render_template("recommend.html")



if __name__=="__main__":
    app.run(debug=True)                   