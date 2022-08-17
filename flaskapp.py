from flask import Flask,render_template,request,jsonify
import util
import sklearn
import pickle
import numpy as np

#model = pickle.load(open('LRModel.pickle','rb'))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get_Car_names')
def get_Car_names():
    response = Jsonify({
        'Car_name': util.get_Car_names()
    })
    #response.headers.add('Access-control-allow-Origin', '*')
    return response

@app.route('/predict_carprice',methods=['POST'])
def predict_carprice():
    car_name = request.form['car_name']
    vehicle_age = int(request.form['vehicle_age'])
    km_driven = int(request.form['km_driven'])
    seller_type = request.form['seller_type']
    if seller_type == "dealer":
        Dealer = 1
    elif seller_type == "individual":
        Individual = 1
    else:
        Trustmark_Dealer  = 1


    response = jsonify({
        'estimated_price':util.get_estimated_price(car_name,vehicle_age,km_driven,seller_type)
    })
    #response.headers.add('Access-control-allow-Origin','*')

    return response


if __name__ == "__main__":
    util.load_saved_artefacts()
    app.run(debug=True)