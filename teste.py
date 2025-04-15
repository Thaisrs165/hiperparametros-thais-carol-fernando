import pandas as pd
import matplotlib.pyplot as plt

# Carregar os três arquivos CSV
arquivo1 = pd.read_csv("data/epsilon_decay.csv", header=None)
arquivo2 = pd.read_csv("data/exploit_only.csv", header=None)
arquivo3 = pd.read_csv("data/explore_only.csv", header=None)

# Configurar o eixo X como o índice das linhas
x1 = range(len(arquivo1))
x2 = range(len(arquivo2))
x3 = range(len(arquivo3))

# Criar o gráfico
plt.figure(figsize=(12, 6))

# Plotar os dados de cada arquivo com cores diferentes
for coluna in arquivo1.columns:
    plt.plot(x1, arquivo1[coluna], label=f"Arquivo 1 - Série {coluna + 1}", color='red', linestyle='--')

for coluna in arquivo2.columns:
    plt.plot(x2, arquivo2[coluna], label=f"Arquivo 2 - Série {coluna + 1}", color='blue', linestyle='-')

for coluna in arquivo3.columns:
    plt.plot(x3, arquivo3[coluna], label=f"Arquivo 3 - Série {coluna + 1}", color='green', linestyle=':')

# Configurações do gráfico
plt.title("Comparação de Dados dos Arquivos CSV")
plt.xlabel("Índice das Linhas")
plt.ylabel("Valores")
plt.legend(loc="best")
plt.grid(True)

# Exibir o gráfico
plt.show()