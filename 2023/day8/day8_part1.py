input = open('day8/input')
steps = input.readline().strip()

nodes = {}

for node in input.readlines():
  try:
    x, y = node.split('=')
    z = tuple([x.strip('()\n ') for x in y.split(',')])
    nodes[x.strip()] = {'L': z[0], 'R': z[1] }
  except ValueError:
    continue

counter=0
cursor = 'AAA'

while cursor != "ZZZ":
  for step in steps:
    cursor = nodes[cursor][step]
    counter+=1
    
print(counter)
