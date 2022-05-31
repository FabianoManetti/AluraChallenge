# -*- coding: utf-8 -*-
"""preprocessamento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fOQoe9Jt2kiKJJDicFrjAqNNZ6DWl-V5
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def pre_processamento(df):
   
    def mapeamento(feature):
        return feature.map({'Sim':1, 'Não':0})

    lista = ['Idoso','Dependentes', 'Parceiro', 'Internet', 'Fatura_Online', 'Mensal','Anual', 
             'Bianual', 'Cartao_credito', 'Boleto_eletronico', 'Boleto_correios', 'Transf_banco']
    df[lista] = df[lista].apply(mapeamento)

    scaler = MinMaxScaler()
    df['Meses_Contrato'] = scaler.fit_transform(df[['Meses_Contrato']])
    df['Gasto_Mensal'] = scaler.fit_transform(df[['Gasto_Mensal']])
    df['Gasto_Total'] = scaler.fit_transform(df[['Gasto_Total']])
    return df

