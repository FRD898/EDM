from sklearn import svm
import pandas as pd
import numpy as np
import sys
import pickle
from sklearn.model_selection import train_test_split
import uuid
import re
import random

def correctNotes(x):
    for i,val in enumerate(x):
      r = re.findall("[0-9]+,[0-9]+", str(val))
      if r:
        x[i] = r[0].replace(',','.')
    return x

def correctPorcentajes(x):
  res = []
  for val in x:
    r = re.findall("[0-9]+", str(val))
    if r:
      val = r[0]
    res.append(val)
  
  return pd.Series(res)


def convertAttributestoNumber(df):
  df = df.replace(['Sí','No'],[1,0])
  df = df.replace(['Femenino','Masculino'],[1,0])
  df = df.replace(['Ciencia de la Computación','Física','Ingeniería Física','Química','Matemática'],[0,1,2,3,4])
  df = df.replace(['Solo','Con mi familia'],[0,1])
  df = df.replace(['Básico','Intermedio','Avanzado'],[0,1,2])
  df = df.replace(['Público','Privado'],[0,1])
  df = df.replace(['Menos de un año','Entre 1 a 2 años','Entre 2 a 3 años','de 3 años a más'],[0,1,2,3])
  df = df.replace(['Ordinario','Cepre-UNI','Escolar u otra opción'],[0,1,2])
  df = df.replace(['A','B','C','D','E','F'],[0,1,2,3,4,5])
  df = df.replace(['Departamento de Lima','Otro departamento'],[0,1])
  return df


def prepareData(data):
  data = data

  columns = {'Código de estudiante':'0',
            'Escuela a la que pertenece':'1', 
            'Edad actual':'2', 
            'Género':'3', 
            '¿Trabajó mientras llevaba el curso de Introducción a la Computación?':'4',
            '¿Vivía solo o con su familia mientras llevaba el curso de Introducción a la Computación?':'5',
            'Lugar de residencia':'6',
            '¿Sabes inglés?':'7',
            "Si tu respuesta fue 'Sí', selecciona tu nivel de Inglés":'8',
            '¿Es su segunda carrera universitaria?':'9',
            '¿Estudió en algún instituto antes de la universidad?':'10',
            '¿Hizo traslado interno o externo?':'11',
            '¿Llevó algún curso relacionado a la programación antes de la universidad?':'12',
            '¿Llevó alguna carrera técnica o universitaria de manera paralela a la UNI?':'13',
            '¿Estudió en un colegio público o privado?':'14',
            'Tiempo de preparación antes de ingresar a la UNI':'15',
            'Nota promedio del examen de admisión(aproximado)':'16',
            'Tipo de ingreso':'17',
            "¿Aprobó el curso de Introducción a la Computación? (Si llevó el curso más de una vez, seleccione 'No')":'18',
            '¿En qué sección estuvo matriculado?':'19',
            '¿Formó parte de algún grupo de deportes?':'20',
            '¿Formó parte de algún grupo estudiantil?(No es necesario que haya sido de manera oficial)':'21',
            '¿Cuántas horas extra de estudio le dedicó al curso de introducción a la Computación?. (Horas por semana de manera aproximada)':'22',
            '¿Qué porcentaje de las clases del curso de Introducción a la Computación faltaste (aproximadamente)?':'23',
            '¿Rindió la primera práctica en el curso de Introducción a la Computación?':'24',
            '¿Rindió la segunda práctica en el curso de Introducción a la Computación?':'25',
            '¿Rindió el examen parcial en el curso de Introducción a la Computación?':'26',
            '¿Participabas en clase(antes del parcial)  del curso de Introducción a la Computación?':'27',
            '¿Presentaste las tareas(antes del parcial) en el curso de Introducción a la Computación?':'28',
            '¿Cuál fue tu promedio de prácticas antes del parcial en el curso de Química 1?':'29',
            '¿Cuál fue tu nota del examen parcial en el curso de Química 1?':'30',
            '¿Cuál fue tu promedio de prácticas antes del parcial en el curso de Física 1?':'31',
            '¿Cuál fue tu nota del examen parcial en el curso de Física 1?':'32',
            '¿Cuál fue tu promedio de prácticas antes del parcial en el curso de Algebra Lineal?':'33',
            '¿Cuál fue tu nota del examen parcial en el curso de Algebra Lineal?':'34',
            '¿Cuál fue tu promedio de prácticas antes del parcial en el curso de Cálculo Diferencial?':'35',
            '¿Cuál fue tu nota del examen parcial en el curso de Cálculo Diferencial?':'36',
            '¿Cuál fue tu promedio de prácticas antes del parcial en el curso de Introducción a la Computación?':'37',
            '¿Cuál fue tu nota del examen parcial en el curso de Introducción a la Computación?':'38',
            '¿Cuál fue tu nota del examen final en el curso de Introducción a la Computación?':'39',
            '¿Cuál fue tu promedio final en el curso de Introducción a la Computación (la primera vez que llevaste)?':'40',
  }
  
  df = data.rename(columns=columns)
  df = convertAttributestoNumber(df)
  df['8'].replace([np.nan],[3],inplace = True)
  df['8'].values


  notas_attr = ['16','29','30','31','32','33','34','35','36','37','38','39','40']

  df[notas_attr]=df[notas_attr].apply(correctNotes,axis=1)

  porcentaje_attr = ['22','23']

 

  df[porcentaje_attr]=df[porcentaje_attr].apply(correctPorcentajes,axis=1)

  df.replace('Casi una hora', '1', inplace=True)
  df.replace('Solo falté en una clase', '5', inplace=True)
  df.replace("8 :'v", "8", inplace=True)
  df.replace("No di", "0", inplace=True)

  df2 = df[51:]
  df = df[:50]
  return df

def Cargar(name):
    return pickle.load(open(f"./models/{name}.sav", 'rb'))

def Predict(data, model):
    model_loaded = Cargar(model)
    salida = Predict(data)
    return salida 