input = open("day9/input")

total = 0
"""Loop thru each sequence"""
for r in input.readlines():

  """Iterate thru until we get have all zeros"""
  seq = list(map(int, r.split()))
  all = [seq]
  while sum(seq) != 0:
    seq = [seq[x]-seq[x-1] for x in range(1,len(seq))]
    all.append(seq)

  """Go back in reverse and extrapolate each sequence with the sum of previous row's first value"""
  next = 0
  for x in range(1,len(all)+1):
    next=all[-x][0]-next
  total+=next

print(total)
