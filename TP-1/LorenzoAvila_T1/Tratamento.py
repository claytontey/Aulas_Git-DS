from xml.etree.ElementTree import tostring

import pandas as pd
import matplotlib.pyplot as plt

# 1 - Lendo arquivos csv e convertendo pra um dataframe
dataframe = pd.read_csv(r"C:\Users\Thinkpad\Desktop\Ciencia de dados\T1\Aulas_Git-DS\TP-1\LorenzoAvila_T1\student_mental_health_burnout (1).csv")

#2 - padronizando para que todos os indices das minhas colunas fiquem minusculas
dataframe.columns = dataframe.columns.str.strip().str.lower()

#3- Remover valores duplicados
#dataframe = dataframe.drop_duplicates(subset="coluna")

#4- Remover coluna vazia
dataframe = dataframe.dropna(axis=1, how = "all")#sufixo "na" remove valores vazios. axis = 1 (colunas)   axis = 0(linhas). how = any (se houver apenas umt ermo vazio)
dataframe = dataframe.dropna(axis=0,thresh = 3,subset= ["student_id","course","year"])#se houver uma linha em que nn tenha ID, curso e ano essa linha é apagada

#5- Tratar os dados
dataframe["student_id"] =dataframe["student_id"].astype(str)
dataframe["age"] = pd.to_numeric(dataframe["age"],errors="coerce")
dataframe["year"] = pd.to_numeric(dataframe["year"],errors = "coerce")




#6- Tratar linhas com valores vazios

dataframe["daily_study_hours"] = dataframe["daily_study_hours"].fillna(dataframe["daily_study_hours"].mean())#caso possua uma linha em q o valor é vazio ele a substitui pela media dos outros elementos da coluna

#7- Padronizar valores de texto
dataframe["gender"] = dataframe ["gender"].str.title()#padronizo para se houver algum gnero escrito como (m)asculino ou MASCULINO ele padronize para (M)asculino (F)eminino etc
dataframe["course"] = dataframe["course"].str.upper()
dataframe["stress_level"]=dataframe["stress_level"].str.title()
dataframe["sleep_quality"] =dataframe["sleep_quality"].str.title()
dataframe["burnout_level"] = dataframe["burnout_level"].str.title()
dataframe["internet_quality"] = dataframe["internet_quality"].str.title()

#Salvando o dataset tratado
dataframe.to_csv("dataset_tratado.csv", index=False)