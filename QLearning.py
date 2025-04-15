import numpy as np
import random
import matplotlib.pyplot as plt

class QLearning:
    def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):
        self.env = env
        self.q_table = np.zeros([env.observation_space.n, env.action_space.n])
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.episodes = episodes

    def select_action_explore(self, state):
        # Apenas explora, sempre escolhe ações aleatórias
        return self.env.action_space.sample()

    def select_action_exploit(self, state):
        # Explora com probabilidade de 10% e explora 90% (baseado na Q-Table)
        rv = random.uniform(0, 1)
        if rv < 0.1:  # Probabilidade de exploração
            return self.env.action_space.sample()
        return np.argmax(self.q_table[state])

    def select_action_decay(self, state):
        # Usa epsilon-decay para alternar entre explorar e explorar
        rv = random.uniform(0, 1)
        if rv < self.epsilon:  # Usa epsilon para decidir a exploração
            return self.env.action_space.sample()
        return np.argmax(self.q_table[state])

    def train(self, select_action, filename, plotFile):
        actions_per_episode = []
        rewards_per_episode = []

        for i in range(1, self.episodes+1):
            (state, _) = self.env.reset()
            rewards = 0
            done = False
            actions = 0

            while not done:
                action = select_action(state)  # Escolhe ação baseado no método
                next_state, reward, done, _, _ = self.env.step(action)

                # Atualiza a Q-Value
                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])
                self.q_table[state, action] = old_value + self.alpha * (reward + self.gamma * next_max - old_value)

                # Atualiza estado e contadores
                state = next_state
                actions += 1
                rewards += reward

            actions_per_episode.append(actions)
            rewards_per_episode.append(rewards)

            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_dec

        # Salvar Q-table e plotar
        np.savetxt(filename, self.q_table, delimiter=',')
        self.plot_results(plotFile, actions_per_episode, rewards_per_episode)

        return self.q_table

    def plot_results(self, plotFile, actions_per_episode, rewards_per_episode):
        # Gerar gráficos para comparação
        plt.figure(figsize=(10, 5))
        plt.plot(actions_per_episode, label='Ações por episódio')
        plt.plot(rewards_per_episode, label='Recompensas por episódio')
        plt.xlabel('Episódios')
        plt.ylabel('Média')
        plt.title('Curva de Aprendizado do Agente')
        plt.legend()
        plt.grid(True)
        plt.savefig(plotFile)
        plt.close()

