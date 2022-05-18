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
    svm = pr.Cargar("randomForest2")
    query = request.args.get('data')
    data = convertDataFrame(query)
    df = pr.prepareData(data)        
    atributos = ['38','28','37','26','34','24','29','25','19']
    
    '''
    Regresión Lineal

    '38' nota del examen parcial en el curso de Introducción a la Computación
    '28' presentar todas las tareas antes del parcial
    '24' Rindió la primera práctica en el curso de Introducción a la Computación
    '37' promedio de practicas Intro a C.
    '26' Rindio el examen parcial de Intro a C.
    '34' nota del examen parcial en el curso de Algebra Lineal
    '29' promedio de prácticas antes del parcial en el curso de Química 1
    '25' Rindió la segunda práctica en el curso de Introducción a la Computación
    '19' En qué sección estuvo matriculado

    PCA

    35: promedio de prácticas antes del parcial en el curso de Cálculo Diferencial	
    11: Hizo traslado interno o externo
    25: Rindió la segunda práctica en el curso de Introducción a la Computación
    8: Nivel de inglés
    5: Vivía solo o con su familia
    19: sección
    17: Tipo de ingreso
    9: segunda carrera universitaria
    10: Estudió en algún instituto antes de la universidad
    36: nota del examen parcial en el curso de Cálculo Diferencial
    20: Formó parte de algún grupo de deportes
    23: Porcentaje de faltas
    29: Promedio de PCs de Quimica antes del parcial
    6: Lugar de residencia

    38, nota del examen parcial en el curso de Introducción a la Computación
    28, nota del examen parcial en el curso de Introducción a la Computación
    37, promedio de prácticas antes del parcial  
    26, Rindió la segunda práctica en el curso de Introducción a la Computación
    34, nota del examen parcial en el curso de Algebra Lineal
    24, Rindió la primera práctica en el curso de Introducción a la Computación
    29, promedio de prácticas antes del parcial en el curso de Química 1

    Matriz de correlación clasificación

    '''
    X = df[atributos]
    y_pred = svm.predict(X)
    res = []
    real = []
    for i,val in enumerate(y_pred):
        print(f'val {val}')
        if val==0.0:
            res.append("desaprobará")
        else:
            res.append("aprobará")
        if df['18'][i]==0.0:
            real.append("desaprobará")
        else:
            real.append("aprobará")
    res = {
        "prediccion": res,
        "real": real

    }
    return jsonify(res)



if __name__ == '__main__':
    app.run(debug = True, port = 4000)