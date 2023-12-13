import re, sys

input = open("day7/input").readlines()
hands = [(x,y) for x,y in [row.split() for row in input]]

card_rank = {
              "A": "0C",
              "K": "0B",
              "Q": "0A",
              "J": "09",
              "T": "08",
              "9": "07",
              "8": "06",
              "7": "05",
              "6": "04",
              "5": "03",
              "4": "02",
              "3": "01",
              "2": "00"
              }

def get_card_score(cards) -> str:
  return "".join([card_rank[y] for y in list(cards)])

def get_hand_score(hand: str) -> str:
  sorted_hand = "".join(sorted(hand.strip()))
  
  """Five of a kind"""
  if len(set(sorted_hand)) == 1:
    return "07"

  """Four of a kind"""
  if re.findall("(\w)\\1{3}", sorted_hand):
    return "06"
  
  """Full house of a kind"""
  if len(set(sorted_hand)) == 2:
    return "05"
    
  """Three of a kind"""
  if re.findall("(\w)\\1{2}", sorted_hand):
    return "04"

  """Two pairs"""
  if len([x for x in re.findall("(\w)\\1{1}", sorted_hand)]) == 2:
    return "03"
  
  """One pair"""
  if re.findall("(\w)\\1{1}", sorted_hand):
    return "02"

  """Uniqe cards"""
  if len(set(sorted_hand)) == 5:
    return "01"


"""
Sort all hands by creating a total score for the hand:

Map each card to a hex value e.g A -> 0C, K-> 0B...
Map the type of hand (pair, full house etc) to a hex value.

Example, hand 32T3K is one pair = "02" + hex value for each card

Combine into a 6-byte string and convert to decimal
"02" + "010008010B" -> 2203318747403
"""
rated_hands = []

for hand, bid in hands:
  a,b = get_hand_score(hand), get_card_score(hand)
  score = int(a+b, 16)
  rated_hands.append((hand,bid, score))

"""Calculate total amount"""
total_amount = 0
rank = 1
for card, bid, _t in sorted(rated_hands, key=lambda x: x[2]):
  total_amount+=int(bid)*rank
  rank+=1

print(total_amount)