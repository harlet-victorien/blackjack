from bj_func import *

import statistics as stat

import csv

import numpy as np

class QLearningAgent:
    def __init__(self, alpha, gamma, epsilon, actions):
        self.alpha = alpha  # Taux d'apprentissage
        self.gamma = gamma  # Facteur de réduction
        self.epsilon = epsilon  # Probabilité d'exploration
        self.actions = actions  # Liste des actions possibles
        self.Q = {}  # Table Q

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploration
            action = np.random.choice(self.actions)
        else:
            # Exploitation
            q_values = [self.Q.get((state, a), 0) for a in self.actions]
            max_q = max(q_values)
            actions_with_max_q = [a for a, q in zip(self.actions, q_values) if q == max_q]
            action = np.random.choice(actions_with_max_q)
            '''# Exploitation
            # Calculer les valeurs Q pour toutes les actions possibles à partir de l'état actuel
            q_values = []
            for action in self.actions:
                q_value = self.Q.get((state, action), 0)  # Récupérer la valeur Q de l'état-action, 0 si inconnue
                q_values.append(q_value)

            # Trouver la valeur Q maximale parmi toutes les actions
            max_q = max(q_values)

            # Trouver toutes les actions ayant une valeur Q égale à la valeur Q maximale
            actions_with_max_q = []
            for action, q_value in zip(self.actions, q_values):
                if q_value == max_q:
                    actions_with_max_q.append(action)

            # Choisir une action au hasard parmi celles ayant la valeur Q maximale
            action = np.random.choice(actions_with_max_q)'''
        return action

    def learn(self, state, action, reward, next_state):
        q_predict = self.Q.get((state, action), 0)
        q_target = reward + self.gamma * max([self.Q.get((next_state, a), 0) for a in self.actions])
        self.Q[(state, action)] = q_predict + self.alpha * (q_target - q_predict)



# Exemple d'utilisation



# Initialisation de l'agent Q-learning
actions = [0, 1]  # Par exemple, 0: rester, 1: tirer
agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.1, actions=actions)

# Nombre de parties à jouer pour l'entraînement
num_episodes = 1000000
results = []
# Boucle d'entraînement
for episode in range(1,num_episodes+1):
    # Réinitialiser l'environnement de jeu
    game = bj(deck)
    state = (game.aScore, game.bScore)  # Exemple de représentation d'état

    while not game.over:
        action = agent.choose_action(state)

        # Appliquer l'action choisie dans le jeu
        game.choice(action)

        # Obtenir la récompense et le nouvel état
        reward = game.win  # À ajuster en fonction de ta structure de récompenses
        new_state = (game.aScore, game.bScore)

        # Apprentissage
        agent.learn(state, action, reward, new_state)

        # Passer au nouvel état
        state = new_state
    results.append(game.win)
    # Afficher des informations si nécessaire (par exemple, tous les 100 épisodes)
    if episode % 10000 == 0:
        
        print(f"Loading: {episode/10000}%, Mean_win: {round(stat.mean(results), 3)}")

'''# Après l'entraînement, tu peux tester l'agent en jouant d'autres parties
# en utilisant la table Q apprise pour choisir des actions.


# Exemple de partie
game = bj(deck)
state = (game.aScore, game.bScore, sum(card == 'A' for card in game.aCards))  # Exemple de représentation d'état
game.show()
#while not game.over:
action = agent.choose_action(state)

# Appliquer l'action choisie dans le jeu
game.choice(action)

# Passer au nouvel état
game.show()'''

