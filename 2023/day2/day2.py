bag = {"red": 12, "green": 13, "blue": 14}
data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')

data = open("day2/input").readlines()

id_sum = 0

# Part 1
for game in data:
  skip_game = False
  game_id, game_sets = game.split(":")
  
  """Loop each set"""
  for game_set in game_sets.split(";"):
    for cube in game_set.split(","):
      number, colour = cube.split()

      """Check if we ran out of cubes for the given game"""
      if int(number) > bag[colour]:
        skip_game = True
        break

  if not skip_game:
    id_sum += int(game_id.split()[-1])

print("Sum: %s"% id_sum)

# Part 2
import math
sum = 0

"""Loop games"""
for game in data:
  game_id, game_sets = game.split(":")

  """Reset count"""
  bag = {"red": 0, "green": 0, "blue": 0}
  
  """Loop each set"""
  for game_set in game_sets.split(";"):
    for cube in game_set.split(","):
      number, colour = cube.split()

      """Store largest number for each colour"""
      if int(number) > bag[colour]:
        bag[colour] = int(number)

  """Multiply numbers and to sum"""
  sum+=math.prod([bag[x] for x in bag.keys()])

print("Sum: %s"% sum)