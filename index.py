import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('./manejoDeDatos/data.csv')


#top 10 canciones bailables
def top10() :
  print('top 10 canciones bailables')
  print('---------------------------------------------------------------------------')
  print(pd.DataFrame(datos).sort_values('danceability').head(10))
  print('---------------------------------------------------------------------------')
  pd.DataFrame(datos['danceability']).head(10).plot()
  plt.show()

#cómo se ven los datos 'danceability', 'energy', 'key', 'loudness' de las top 10 canciones likeadas
def datosLiked() :
  df2 = pd.DataFrame(datos, columns=['liked', 'danceability', 'energy', 'key', 'loudness'])
  print('top 10 canciones bailables')
  print('---------------------------------------------------------------------------')
  print(df2.loc[df2['liked'] == 1].head(10))
  print('---------------------------------------------------------------------------')
  pd.DataFrame(df2.loc[df2['liked'] == 1].head(10)).plot()
  plt.show()

#valor de energy más alto
def datosEnergy() :
  print('---------------------------------------------------------------------------')
  print(pd.DataFrame(datos)['energy'].max())
  print('---------------------------------------------------------------------------')
  pd.DataFrame(datos)['energy'].plot(kind='hist')
  plt.show()

top10()
datosLiked()
datosEnergy()