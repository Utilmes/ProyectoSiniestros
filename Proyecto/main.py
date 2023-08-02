#%%

import pandas as pd
import matplotlib.pyplot as plt


# comunas = ["Retiro, San Nicolás, Puerto Madero, San Telmo, Montserrat y Constitución",
#             "Recoleta", "Balvanera y San Cristóbal","La Boca, Barracas, Parque Patricios y Nueva Pompeya",
#             "Almagro y Boedo.", "Caballito", "Flores y Parque Chacabuco.", "Villa Soldati, Villa Riachuelo y Villa Lugano",
#             "Liniers, Mataderos y Parque Avellaneda", "Villa Real, Monte Castro, Versalles, Floresta, Vélez Sarsfield y Villa Luro",
#             "Villa General Mitre, Villa Devoto, Villa del Parque y Villa Santa Rita",
#             "Coghlan, Saavedra, Villa Urquiza y Villa Pueyrredón", "Núñez, Belgrano y Colegiales",
#             "Palermo", "Chacarita, Villa Crespo, La Paternal, Villa Ortúzar, Agronomía y Parque Chas"]

df = pd.read_csv(".\Victimas_siniestros_2015-2018.csv")


# print(df.info())

# Identifico la cantidad de comunas y accidentes en cada una
totalComunas = df['comuna']

accidentesPorComuna = totalComunas.value_counts()

print(accidentesPorComuna)

# Una vez encontrada la info la preparo para presentar en un bar graph

plt.figure(figsize=(8, 6)) 

plt.xlabel('Comunas')

plt.ylabel('Cantidad de accidentes') 

plt.title("Accidentes de transito por comunas de Buenos Aires(2015-2018)")

accidentesPorComuna.plot(kind='barh').invert_yaxis()

# Bar graph presentado
plt.show()


#%%

import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(".\Victimas_siniestros_2015-2018.csv")

#Primero identifico la cantidad de choques que hubo en general y luego en cada tipo de calle

cantidadChoques = df['tipo_calle'].value_counts()

choquesAutopista = df[(df['tipo_calle'] == 'autopista')]

choquesCalle = df[(df['tipo_calle'] == 'calle')]

choquesAvenida = df[(df['tipo_calle'] == 'avenida')]


# print(len(choquesAutopista))
# print(len(choquesCalle))
# print(len(choquesAvenida))
print(cantidadChoques)

# Aca preparo los datos para presentarlos en un pie chart con los respectivos porcentajes de cada lugar

plt.figure(figsize=(8, 6)) 

plt.title("Accidentes de transito en Buenos Aires(2015-2018)")

cantidadChoques.plot(kind='pie', autopct='%1.1f%%')
plt.show()

#%%

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(".\Victimas_siniestros_2015-2018.csv")

# Aca busco cuales fueron la cantidad de choques multiples en cada lugar

choquesMultiples = df[df['tipo_colision1'] == 'multiple']
choquesMultiplesAutopista = df[(df['tipo_colision1'] == 'multiple') & (df['tipo_calle'] == 'autopista')]


labels = 'Moto-Auto', 'auto-peaton', 'auto-auto', 'multiple','moto-peaton', 'bici-auto', 'moto-moto', 'otros'
sizes = [35,17.7,20,13,4.5,4.3,2,3.5]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

print(df['tipo_colision1'].value_counts())

print(f"Los choques multiples en los años mencionados fueron {len(choquesMultiples)} de los cuales {len(choquesMultiplesAutopista)} fueron en autopistas")

# %%
