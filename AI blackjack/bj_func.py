#go créer un bot qui jour au blackjack


#* imports                                              

import random as rd


#* functions                                            



# Fonctions
def get(deck):
    index = rd.randint(0, len(deck) - 1)
    picked_card = deck[index]
    del(deck[index])
    return picked_card

def score(cards):
    total_score = 0
    aces = 0
    for card in cards:
        if isinstance(card, int):
            total_score += card
        elif card in ['J', 'Q', 'K']:
            total_score += 10
        else:
            aces += 1
    for _ in range(aces):
        if total_score + 11 <= 21:
            total_score += 11
        else:
            total_score += 1
    return total_score

# Classe Blackjack
class bj():
    def __init__(self, deck):
        self.deck = deck.copy()
        self.aCards = [get(self.deck)] + [get(self.deck)]
        self.bCards = [get(self.deck)]
        self.aScore = score(self.aCards)
        self.bScore = score(self.bCards)
        self.win = 0
        self.over = 0

    def choice(self, choice):
        if choice == 0:
            self.over = 1
            self.dealer()
            self.bScore = score(self.bCards)
            if self.bScore > 21 or self.aScore > self.bScore:
                self.win = 1
            elif self.aScore < self.bScore:
                self.win = -1
            else:
                self.win = 0
        else:
            self.aCards.append(get(self.deck))
            self.aScore = score(self.aCards)
            if self.aScore > 21:
                self.win = -1
                self.over = 1

    def dealer(self):
        while self.bScore < 16:
            self.bCards.append(get(self.deck))
            self.bScore = score(self.bCards)

    def reset(self):
        self.deck = deck.copy()
        self.aCards = [get(self.deck)] + [get(self.deck)]
        self.bCards = [get(self.deck)]
        self.aScore = score(self.aCards)
        self.bScore = score(self.bCards)
        self.win = 0
        self.over = 0

    def play(self):
        #print("Début du jeu")  # Débogage
        while not self.over:
            #print("Boucle de jeu en cours")  # Débogage
            #self.show()
            choice=int(input("Choisir action (0: Rester, 1: Tirer): "))
            self.choice(choice)
        


    def show(self):
        print("\n\n\n")
        print("Vos cartes :        ", self.aCards, ", score :", self.aScore)
        print("Cartes du croupier :", self.bCards, ", score :", self.bScore)


class bj_h:
    def __init__(self, deck):
        self.deck = deck.copy()
        self.aCards = [get(self.deck)] + [get(self.deck)]
        self.bCards = [get(self.deck)]
        self.aScore = score(self.aCards)
        self.bScore = score(self.bCards)
        self.win = 0
        self.over = 0

    def choice(self, choice):
        if choice == 0:
            self.over = 1
            self.dealer()
            self.bScore = score(self.bCards)
            if self.bScore > 21 or self.aScore > self.bScore:
                self.win = 1
            elif self.aScore < self.bScore:
                self.win = -1
            else:
                self.win = 0
        else:
            self.aCards.append(get(self.deck))
            self.aScore = score(self.aCards)
            if self.aScore > 21:
                self.win = -1
                self.over = 1

    def dealer(self):
        while self.bScore < 16:
            self.bCards.append(get(self.deck))
            self.bScore = score(self.bCards)

    def reset(self):
        self.deck = deck.copy()
        self.aCards = [get(self.deck)] + [get(self.deck)]
        self.bCards = [get(self.deck)]
        self.aScore = score(self.aCards)
        self.bScore = score(self.bCards)
        self.win = 0
        self.over = 0

    def play(self):
        print("Début du jeu")  # Débogage
        while not self.over:
            print("Boucle de jeu en cours")  # Débogage
            self.show()
            try:
                print("Demande d'entrée utilisateur")  # Débogage
                choice = input("Choisir action (0: Rester, 1: Tirer): ")
                choice = int(choice)
                if choice in [0, 1]:
                    self.choice(choice)
                else:
                    print("Entrée invalide. Veuillez choisir 0 ou 1.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre valide.")
        self.show()
        if self.win == 1:
            print("Vous avez gagné !")
        elif self.win == 0:
            print("Match nul.")
        else:
            print("Vous avez perdu.")
        print("\n")


    def show(self):
        print("\n\n\n")
        print("Vos cartes :        ", self.aCards, ", score :", self.aScore)
        print("Cartes du croupier :", self.bCards, ", score :", self.bScore)





# Initialisation du deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4




