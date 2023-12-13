import math
games = {}
all_copies = {}
sum=0

"""Create map with game id as index key"""
for row in open("./day4/input").readlines():
  col1, col2= row.split('|')
  game, drawed = col1.split(':')

  games[game.split()[-1]] = (drawed.split(),col2.split())

"""Loop games and count number of cards"""
for game in games.keys():
  winners = [x for x in games[game][0] if x in games[game][1]]

  """Add current card to our list, even if it had no winners!"""
  try:
    all_copies[game]+=1
  except KeyError:
    all_copies[game]=1

  """For each copy of current card, add the won cards in into the map"""
  for y in range(1,all_copies[game]+1):
    for x in range(1,len(winners)+1):
      next = str(int(game) + x)
      if next in games.keys():  
        try:
          all_copies[next]+=1
        except KeyError:
          all_copies[next]=1

  sum+=all_copies[game]
  
print("Sum: %s"% sum)
