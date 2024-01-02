import csv
import statistics as stat
from bj_func import*
import numpy as np
# Étape 1: Lire le fichier CSV et stocker les valeurs Q dans un dictionnaire
Q = {}
with open('q_table_test.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Ignorer l'en-tête si présent
    for row in reader:
        etat, action, valeur_q = row[0], int(row[1]), float(row[2])
        Q[(etat, action)] = valeur_q


# Boucle de test

num_episodes = 10000
results = []
for episode in range(1,num_episodes+1):
    # Réinitialiser l'environnement de jeu
    game = bj(deck)
    state = (game.aScore, game.bScore, sum(card == 'A' for card in game.aCards))  # Exemple de représentation d'état
    actions=[0,1]
    while not game.over:
        q_values = [Q.get((state, a), 0) for a in actions]
        max_q = max(q_values)
        actions_with_max_q = [a for a, q in zip(actions, q_values) if q == max_q]
        action = np.random.choice(actions_with_max_q)
        # Appliquer l'action choisie dans le jeu
        game.choice(action)

        # Obtenir le nouvel état
        new_state = (game.aScore, game.bScore, sum(card == 'A' for card in game.aCards))

        # Passer au nouvel état
        state = new_state

    results.append(game.win)
print(f"Après {num_episodes} tests on a: Mean_win: {round(stat.mean(results), 3)}")
