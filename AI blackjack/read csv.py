import csv

# Ouvrir un fichier CSV en mode lecture
with open('q_table.csv', 'r') as file:
    reader = csv.reader(file)
    # Lire chaque ligne du fichier CSV
tab=[]
for (etat, action), valeur_q in reader.items():
        tab.append([etat, action, round(valeur_q,3)])
tab=sorted(tab, key=lambda x: (x[0][0], x[0][1]))
for row in tab:
    print(row)  # Chaque 'row' est une liste représentant une ligne du tableau

