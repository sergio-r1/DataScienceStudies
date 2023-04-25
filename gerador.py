import pandas as pd
import random as rd
import os

def gerador(nome, diretorio):
    tudo = os.path.join(diretorio, nome)
    acc = list()
    for i in range(0, 1000):
        if i< 300:
            df = pd.DataFrame({'x': [i], 'y': [rd.uniform(0.0, 0.3)]})
        elif 301 < i < 600:
            df = pd.DataFrame({'x': [i], 'y': [rd.uniform(0.3, 0.5)]})
        else:
            df = pd.DataFrame({'x': [i], 'y': [rd.uniform(0.5, 1.0)]})
        acc.append(df)
    df = pd.concat(acc)
    df.to_csv(tudo, index=False)



#gerador('reglin.csv', '/home/nikola/MeuLab/RegressaoLinear/')
gerador('reglog1.csv', '/home/nikola/MeuLab/RegressaoLogistica/')