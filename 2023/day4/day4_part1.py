import math
data = open("./day4/input").readlines()
sum=0
for row in data:
  col1, col2= row.split('|')

  drawed = col1.split(':')[-1].split()
  played = col2.split()

  winners = [int(x) for x in played if x in drawed]

  if winners:
    score = 1
    for x in range(len(winners)-1):
      score*=2
  
    sum+=score

print("Sum: %s"% sum)