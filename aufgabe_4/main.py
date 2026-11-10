from collections import Counter
import random
from typing import Callable, Dict, List

SUITS: List[str] = ["Hearts", "Diamonds", "Spades", "Clubs"]
RANKS: Dict[str, int] = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:

  def __init__(self, rank: str, suit: str) -> None:
    self.rank: str = rank
    self.suit: str = suit
    self.value: int = RANKS[rank]

  def __repr__(self) -> str:
    return f"{self.rank} of {self.suit}"


def create_deck() -> List[Card]:
  return [Card(rank, suit) for suit in SUITS for rank in RANKS]


def draw_hand(deck: List[Card], n: int = 5) -> List[Card]:
  return random.sample(deck, n)


def is_straight(values: List[int]) -> bool:
  sa = sorted(list(set(values)))
  if len(sa) != 5:
    return False
  if sa[-1] - sa[0] == 4:
    return True
  if sa == [2, 3, 4, 5, 14]:
    return True
  return False


def has_royal_flush(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  suits = [card.suit for card in hand]
  return len(set(suits)) == 1 and sorted(values) == [10, 11, 12, 13, 14]


def has_straight_flush(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  suits = [card.suit for card in hand]
  return len(set(suits)) == 1 and is_straight(values)


def has_four_of_a_kind(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  counts = Counter(values)
  return 4 in counts.values()


def has_full_house(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  counts = Counter(values)
  return 3 in counts.values() and 2 in counts.values()


def has_flush(hand: List[Card]) -> bool:
  suits = [card.suit for card in hand]
  return len(set(suits)) == 1


def has_straight(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  return is_straight(values)


def has_three_of_a_kind(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  counts = Counter(values)
  return 3 in counts.values() and 2 not in counts.values()


def has_two_pair(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  counts = Counter(values)
  return list(counts.values()).count(2) == 2


def has_pair(hand: List[Card]) -> bool:
  values = [card.value for card in hand]
  counts = Counter(values)
  return (
      list(counts.values()).count(2) == 1
      and 3 not in counts.values()
      and 4 not in counts.values()
  )


COMBINATIONS: Dict[str, Callable[[List[Card]], bool]] = {
    "Royal Flush": has_royal_flush,
    "Straight Flush": has_straight_flush,
    "Four of a Kind": has_four_of_a_kind,
    "Full House": has_full_house,
    "Flush": has_flush,
    "Straight": has_straight,
    "Three of a Kind": has_three_of_a_kind,
    "Two Pair": has_two_pair,
    "Pair": has_pair,
}


def evaluate_hand(hand: List[Card]) -> str:
  for name, function in COMBINATIONS.items():
    if function(hand):
      return name
  return "High Card / Other"


def simulate_poker(num_games: int = 100000) -> None:
  statistics: Dict[str, int] = {name: 0 for name in COMBINATIONS.keys()}
  statistics["High Card / Other"] = 0

  print(f"Starting simulation of {num_games:,} games...\n")

  for _ in range(num_games):
    deck = create_deck()
    hand = draw_hand(deck, 5)
    combo = evaluate_hand(hand)
    statistics[combo] += 1

  print("Results:")
  for combo, count in statistics.items():
    percent = (count / num_games) * 100
    print(f"- {combo}: {count} times ({percent:.4f} %)")


if __name__ == "__main__":
  simulate_poker(100000)