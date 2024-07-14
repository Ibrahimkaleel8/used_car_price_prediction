import json
import pickle
import numpy as np

__car_name = None
__data_columns = None
__model = None

def get_estimated_price(car_name,vehicle_age,km_driven,seller_type):
    try:
        loc_index = __data_columns.index(car_name.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = vehicle_age
    x[1] = km_driven
    x[2] = seller_type

    if loc_index >= 0:
        x[loc_index] = 1

    
    return  round(__model.predict([x])[0],2)

def get_Car_names():
    return __car_name

def load_saved_artefacts():
    #print("loading artifacts start")
    global __data_columns
    global __car_name
    global __model

    with open("./artefacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __car_name = __data_columns[3:]

    with open("./artefacts/RFModel.pickle",'rb') as f:
        __model = pickle.load(f)
    #print("loading saved artifacts.done")

if __name__ == '__main__':
    load_saved_artefacts()
    # print(get_Car_names())
    print(get_estimated_price('Ford Ecosport', 6, 30000, 1))
    