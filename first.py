


import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_excel (r'C:\Users\diego\Desktop\2_Vendas - Dados.xlsx')
#for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df)



#Adiciona a constante no modelo
x = sm.add_constant(x)




X = df["RM"]
y = target["MEDV"]