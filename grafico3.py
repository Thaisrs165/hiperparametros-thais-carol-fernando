import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carregar os arquivos (use seus próprios arquivos .csv ou importe via Colab)
# Exemplo para importar arquivos no Colab:


# Após fazer upload dos arquivos, leia-os
explore_only = pd.read_csv('data/explore_only.csv')
exploit_only = pd.read_csv('data/exploit_only.csv')
epsilon_decay = pd.read_csv('data/epsilon_decay.csv')

# Calcular média e desvio padrão das recompensas por episódio
mean_explore = explore_only.mean()
std_explore = explore_only.std()

mean_exploit = exploit_only.mean()
std_exploit = exploit_only.std()

mean_decay = epsilon_decay.mean()
std_decay = epsilon_decay.std()

episodes = np.arange(1, len(mean_explore) + 1)

# Criar DataFrame para plotagem com sombras (área de desvio padrão)
sns.set(style="whitegrid", font_scale=1.2)
plt.figure(figsize=(12, 6))

# Exploração total
plt.plot(episodes, mean_explore, label='Exploração Total (ε = 1.0)', marker='o')
plt.fill_between(episodes, mean_explore - std_explore, mean_explore + std_explore, alpha=0.2)

# Exploração 10% / Exploração 90%
plt.plot(episodes, mean_exploit, label='Exploração 90% / Exploração 10% (ε = 0.1)', marker='s')
plt.fill_between(episodes, mean_exploit - std_exploit, mean_exploit + std_exploit, alpha=0.2)

# Exploração com decaimento
plt.plot(episodes, mean_decay, label='Exploração com Decaimento (ε decrescente)', marker='^')
plt.fill_between(episodes, mean_decay - std_decay, mean_decay + std_decay, alpha=0.2)

# Linha da política ótima
plt.axhline(y=4.1, color='black', linestyle='--', label='Política Ótima (V*)')

plt.xlabel('Episódios')
plt.ylabel('Recompensa Média')
plt.title('Curva de Aprendizado - Estratégias de Escolha de Ação')
plt.legend()
plt.tight_layout()
plt.show()
