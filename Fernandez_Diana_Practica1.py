#!/usr/bin/env python
# coding: utf-8

# # Análisis de Regresión Lineal: Relación entre Edad Gestacional y Peso al Nacer
# 
# 
# Universidad Nacional Autónoma de México <br> 
# Ciencias de Datos <br>
# Estadística y Probabilidad de Datos <br>
# A cargo del Dr. Roberto Barcenas <br>
# Por Diana Fernández Madrigal<br>
# 
# ## Solución a Práctica 1
# 
# En este análisis, se explorará la relación entre la edad gestacional y el peso al nacer. Para ello, se utilizará un enfoque de regresión lineal. El conjunto de datos 'Birthweight' contiene información sobre 42 bebés al nacer, donde la variable dependiente es el peso al nacer en libras, y la variable independiente es la edad gestacional en semanas.
# 

# # Importación de Bibliotecas
# 

# In[10]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


# # Carga de Datos
# 

# In[11]:


data = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
    'Gestation': [44, 40, 41, 44, 42, 38, 40, 42, 38, 38, 41, 40, 38, 41, 40, 37, 39, 34, 39, 33, 40, 41, 37, 39, 37, 35, 33, 41, 40, 40, 38, 39, 39, 45, 39, 41, 40, 39, 38, 41, 35, 40],
    'Birthweight': [4.55, 4.32, 4.1, 4.07, 3.94, 3.93, 3.77, 3.65, 3.63, 3.42, 3.35, 3.27, 3.23, 3.2, 3.15, 3.11, 3.03, 2.92, 2.9, 2.65, 3.64, 3.14, 2.78, 2.51, 2.37, 2.05, 1.92, 4.57, 3.59, 3.32, 3, 3.32, 2.74, 3.87, 3.86, 3.55, 3.53, 3.41, 3.18, 3.19, 2.66, 2.75]
})



# In[3]:


data 


# # Gráfico de dispersión
# 

# In[12]:


sns.scatterplot(x='Gestation', y='Birthweight', data=data)
plt.title('Relación entre Edad gestacional y Peso al nacer')
plt.xlabel('Edad gestacional (semanas)')
plt.ylabel('Peso al nacer (libras)')
plt.show()


# In[20]:


#Modelo 

f"Peso al Nacer = {intercepto:.4f} + {pendiente:.4f} * Edad Gestacional"


# In[28]:


#Coeficientes
intercepto, pendiente = model.params[0], model.params[1]

print(intercepto,pendiente)


# # Análisis
# 
# 
# El modelo de regresión lineal obtenido es el siguiente:
# 
# \[ Peso\ al\ Nacer = -3.0289 + 0.1618 \times Edad\ Gestacional \]
# 
# 
# La pendiente (\(0.1618\)) indica que, en promedio, el peso al nacer aumenta en 0.1618 libras por cada semana adicional de edad gestacional. El intercepto (\(-3.0289\)) representa el peso al nacer cuando la edad gestacional es cero.
# El coeficiente de determinación (\(R^2 = 0.502\)) sugiere que aproximadamente el 50.2% de la variabilidad en el peso al nacer puede explicarse por la edad gestacional.
# 

# In[24]:


#Intervalo de confianza

intervalo_confianza = model.conf_int(alpha=0.05)
print("\n\nIntervalos de confianza al 95% para los parámetros de la regresión:")
print(intervalo_confianza)


# In[27]:


#Prueba de hipótesis y significancia
pruebas_hipotesis = model.summary()
print(pruebas_hipotesis)


# In[17]:


descriptive_stats = data[['Gestation', 'Birthweight']].describe()
print(descriptive_stats)


# 
# Si se enfoca el resultado en el análisis de regresión, se observa una relación significativa entre la edad gestacional y el peso al nacer.La pendiente positiva indica que, en promedio, el peso al nacer tiende a aumentar a medida que la edad gestacional aumenta.Los resultados de las pruebas de hipótesis respaldan la significancia de la regresión.
# En conclusión, existe una relación lineal positiva entre la edad gestacional y el peso al nacer, lo que sugiere que un aumento en la edad gestacional está asociado con un aumento en el peso al nacer.
# 
