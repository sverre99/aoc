import  sys

data = open("day5/input")
seed_raw = list(map(int,data.readline().split(":")[-1].split()))
seeds = [[(seed_raw[x],seed_raw[x]+seed_raw[x+1])] for x in range(0,len(seed_raw),2)]

print("Seed ranges: %s"% str(seeds))
mapping = {}
locations = []

def split_n_strip(x):
  return x.split(":")[0].strip("\n").split()[0]

"""Create mappings"""
temp_map = [ x.split(":") for x in "".join(data.readlines()).split("\n\n")]

for j in temp_map:
  key, values = (split_n_strip(j[0]), [list(map(int, x.split())) for x in j[1].split("\n") if not len(x) == 0])
  mapping[key] = values

def map_ranges(key :str, seeds: list(())) -> int:
  new_ranges = []

  while seeds:
    s, e = seeds.pop()
    for dest, src, offset in mapping[key]:
      os = max(src, s)
      oe = min(src + offset, e)

      if os < oe:
        new_ranges.append((os - src + dest, oe - src + dest))
        if os > s:
          seeds.append((s, os))
        if e > oe:
          seeds.append((oe, e))
        break
    else:
      new_ranges.append((s, e))

  return new_ranges

locations = []
for seed_range in seeds:
  x = map_ranges("seed-to-soil",seed_range)
  x = map_ranges("soil-to-fertilizer",x)
  x = map_ranges("fertilizer-to-water",x)
  x = map_ranges("water-to-light",x)
  x = map_ranges("light-to-temperature",x)
  x = map_ranges("temperature-to-humidity",x)
  x = map_ranges("humidity-to-location",x)

  locations.extend(x)

print(locations)
print(min(locations)[0])