import re, sys

input = open("day7/input").readlines()
hands = [(x,y) for x,y in [row.split() for row in input]]

card_rank = {
              "A": "0D",
              "K": "0C",
              "Q": "0B",
              "J": "00",
              "T": "09",
              "9": "08",
              "8": "07",
              "7": "06",
              "6": "05",
              "5": "04",
              "4": "03",
              "3": "02",
              "2": "01",
              }

def get_card_score(cards) -> str:
  return "".join([card_rank[y] for y in list(cards)])

def get_hand_score(hand: str) -> str:
  cards = "".join(sorted(hand.strip()))
  
  """Five of a kind"""
  if len(set(cards)) == 1:
    return "07"

  """Four of a kind"""
  if re.findall("(\w)\\1{3}", cards):
    return "06"
  
  """Full house of a kind"""
  if len(set(cards)) == 2:
    return "05"
    
  """Three of a kind"""
  if re.findall("(\w)\\1{2}", cards):
    return "04"

  """Two pairs"""
  if len([x for x in re.findall("(\w)\\1{1}", cards)]) == 2:
    return "03"
  
  """One pair"""
  if re.findall("(\w)\\1{1}", cards):
    return "02"

  """Uniqe cards"""
  if len(set(cards)) == 5:
    return "01"


"""
Sort all hands by creating a total score for the hand:

Map each card to a hex value e.g A -> 0C, K-> 0B...
Map the type of hand (pair, full house etc) to a hex value.

Example, hand 32T3K is one pair = "02" + hex value for each card

Combine into a 6-byte string and convert to decimal
"02" + "010008010B" -> to hex string -> "x02010008010B" -> to decimal => 2203318747403
"""
rated_hands = []

for cards, bid in hands:

  """If we have a joker, check all possible outcomes and pick the one with highest rank"""
  if "J" in cards:
    outcomes = [(x,get_hand_score(cards.replace("J", x))) for x in card_rank.keys()]
    a = sorted(outcomes, key=lambda x: x[1])[-1][1]
  else:
    a = get_hand_score(cards)

  b = get_card_score(cards)
  score = int(a+b, 16)
  rated_hands.append((cards,bid,score))

"""Calculate total amount"""
total_amount = 0
rank = 1
for card, bid, _t in sorted(rated_hands, key=lambda x: x[2]):
  total_amount+=int(bid)*rank
  rank+=1

print(total_amount)