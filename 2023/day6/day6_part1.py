import math
input = open("./day6/input").readlines()
races = [list(map(int,x)) for x in [input[0].split(":")[-1].split(), input[-1].split(":")[-1].split()]]

winners = []
for t in races[0]:
  winners.append(len([x*(t-x) for x in range(t) if x*(t-x) > races[1][races[0].index(t)]]))
  
print(math.prod(winners))