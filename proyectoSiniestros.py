#%%
import pandas as pd

df = pd.read_csv('Victimas_siniestros_2015-2018.csv')

df.head()

# %%

#Armo un diccionario para crear una nueva columna que tenga los meses del año convertidos de numero a nombre
mapeo_meses = {
  1.0: 'Enero',
  2.0: 'Febrero',
  3.0: 'Marzo',
  4.0: 'Abril',
  5.0: 'Mayo',
  6.0: 'Junio',
  7.0: 'Julio',
  8.0: 'Agosto',
  9.0: 'Septiembre',
  10.0: 'Octubre',
  11.0: 'Noviembre',
  12.0: 'Diciembre'
}

df['mes_convertido'] = df['mes'].replace(mapeo_meses)

df.head()

# %%
import matplotlib.pyplot as plt 

#Armo un dataframe con el conteo de valores de cada mes

conteo_mes = df['mes_convertido'].value_counts()

#Armo el gráfico. Me lo hizo el ChatGPT

plt.figure(figsize=(8, 6))  
plt.barh(conteo_mes.index, conteo_mes) # eje y / eje x
plt.gca().invert_yaxis()
plt.xlabel('Cantidad')
plt.ylabel('Meses') 
plt.title('¿En que meses ocurren mas choques en la ciudad de Buenos Aires?')
plt.show()

# %%
#Armo un dataframe con el conteo de valores de cada año

conteo_año = df['periodo'].value_counts()

#Armo el gráfico. Me lo hizo el ChatGPT. No me quedó bien, me genera fracciones entre año y año

plt.figure(figsize=(8, 6))  
plt.bar(conteo_año.index, conteo_año)
plt.xlabel('Año')
plt.ylabel('Cantidad') 
plt.title('¿En que año ocurrieron mas choques en la ciudad de Buenos Aires?')
plt.show()
# %%

#Armo un nuevo dataframe con las dos columnas para preparar la linea de tiempo

df_temporal = df.loc[:, ['mes', 'periodo']]
print(df_temporal)

#Les saco los nulls, no estoy seguro de que funcione

# %%

df_temporal.fillna(0)
df_temporal.isnull().sum()

# %%

#Armo un nuevo dataframe con el resultado de los conteos

df_comparacion = df_temporal.value_counts().reset_index(name='count')
print(df_comparacion)

# %%

#Ordeno los resultados primero por periodo y despues por mes

df_comparacion_ordenada = df_comparacion.sort_values(by=['periodo', 'mes'])

print(df_comparacion_ordenada)

# %%

# - - - - - - - - - - - - - - - - - - - - - 

#%%

# Hay algun genero predominante entre las victimas?

df.head()
# %%

df['sexo'].value_counts()
# %%

# Cual es el participante acusado mas frecuente?

df.head()
# %%

df['rol'].value_counts()
# %%

df['participantes_victimas'].value_counts()
# %%

df['participantes_acusados'].value_counts()
# %%
