import sys
sys.path.insert(0, '../../')
from flask import Flask, jsonify,request
from flask_cors import CORS
import pickle
from sklearn import svm
import pandas as pd
import numpy as np
from prediction import prediction as pr
import io
import json

app = Flask(__name__)
CORS(app)
model = pickle.load(open("./models/svm.sav", 'rb'))
#result = model.predict([np.array([0,5,5,0])])
#print(result)
def convertDataFrame(frontData):
    '''
        Recibe una lista de filas(listas) 
    '''
    data = json.loads(frontData)
    columnas = data[0]

    dict = {}
    for i in columnas[1:]:
        dict[str(i)] = []

    for row in data[1:]:
        for name,col in zip(columnas[1:],row[1:]):
            dict[name].append(col)

    df = pd.DataFrame.from_dict(dict)
    return df

@app.route('/search')
def searchDocs():
    svm = pr.Cargar("svm")
    query = request.args.get('data')
    data = convertDataFrame(query)
    df = pr.prepareData(data)        
    atributos = ['38','28','37','26','34','24','29']
    X = df[atributos]
    y_pred = svm.predict(X)
    res = []
    for val in y_pred:
        print(f'val {val}')
        if val==0.0:
            res.append("desaprobará")
        else:
            res.append("aprobará")
    res = {
        "prediccion": res
    }
    return jsonify(res)



if __name__ == '__main__':
    app.run(debug = True, port = 4000)