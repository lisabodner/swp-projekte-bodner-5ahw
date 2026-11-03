import random
from collections import Counter

SUITS = ['Herz', 'Karo', 'Pik', 'Kreuz']
RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, '10': 10, 'Bube': 11, 'Dame': 12, 'König': 13, 'Ass': 14}


class Karte:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANKS[rank]

    def __repr__(self):
        return f"{self.rank} von {self.suit}"


def erstelle_deck():
    return [Karte(rank, suit) for suit in SUITS for rank in RANKS]


def ziehe_haende(deck, n=5):
    return random.sample(deck, n)


from collections import Counter


def hat_full_house(hand):
    werte = [karte.value for karte in hand]
    zaehlung = Counter(werte)
    return 3 in zaehlung.values() and 2 in zaehlung.values()

def hat_drilling(hand):
    werte = [karte.value for karte in hand]
    zaehlung = Counter(werte)
    return 3 in zaehlung.values() and 2 not in zaehlung.values()

def hat_zwei_paare(hand):
    werte = [karte.value for karte in hand]
    zaehlung = Counter(werte)
    return list(zaehlung.values()).count(2) == 2

def hat_paar(hand):
    werte = [karte.value for karte in hand]
    zaehlung = Counter(werte)
    return list(zaehlung.values()).count(2) == 1 and 3 not in zaehlung.values() and 4 not in zaehlung.values()


KOMBINATIONEN = {
    "Full House": hat_full_house,
    "Drilling": hat_drilling,
    "Zwei Paare": hat_zwei_paare,
    "Paar": hat_paar,
}


def evaluiere_hand(hand):
    for name, funktion in KOMBINATIONEN.items():
        if funktion(hand):
            return name
    return "High Card / Sonstige"


def simuliere_poker(anzahl_spiele=100000):
    statistik = {name: 0 for name in KOMBINATIONEN.keys()}
    statistik["High Card / Sonstige"] = 0

    print(f"Starte Simulation von {anzahl_spiele:,} Spielen...")

    for _ in range(anzahl_spiele):
        deck = erstelle_deck()
        hand = ziehe_haende(deck, 5)
        kombi = evaluiere_hand(hand)
        statistik[kombi] += 1

    print("\nErgebnisse:")
    for kombi, anzahl in statistik.items():
        prozent = (anzahl / anzahl_spiele) * 100
        print(f"- {kombi}: {anzahl} mal ({prozent:.4f} %)")


if __name__ == "__main__":
    simuliere_poker(100000)