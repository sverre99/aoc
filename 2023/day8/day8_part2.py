import re
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
cursors = [x for x in nodes.keys() if x[2] == "A"]
print("Start: %s "% cursors)

# TODO: Solution does not work, need to revisit and use lcm()
while list(set([x[2] for x in cursors])) != ['Z']:
  cur = "".join([x[2] for x in cursors])
  if len(re.findall('Z', cur)) > 3:
    print(cursors)
  for step in steps:
    next_cursors = []
    for cursor in cursors:
      next_cursors.append(nodes[cursor][step])
    cursors = next_cursors
    counter+=1

print("End: %s"% cursors)
print(counter)
