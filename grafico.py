import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados dos arquivos CSV
data_010 = pd.read_csv('actions_taxidriver_010.csv')
data_040 = pd.read_csv('actions_taxidriver_040.csv')
data_080 = pd.read_csv('actions_taxidriver_080.csv')

# Preparar o gráfico
plt.figure(figsize=(10, 6))

# Plotando cada conjunto de dados usando colunas específicas dos arquivos CSV
plt.plot(data_010['Bloco'], data_010['Media_de_Recompensas'], label='alpha = 0.10')
plt.plot(data_040['Bloco'], data_040['Media_de_Recompensas'], label='alpha = 0.40')
plt.plot(data_080['Bloco'], data_080['Media_de_Recompensas'], label='alpha = 0.80')

# Adicionando títulos e rótulos dos eixos
plt.title('Rewards vs Episodes - Varying alpha hyperparameter')
plt.xlabel('Episodes (Média a cada 10 episodes))')
plt.ylabel('Rewards Average Sum (Média de Recompensas)')

# Exibindo a legenda e a grade no gráfico
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.show()