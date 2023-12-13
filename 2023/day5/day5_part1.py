import threading, sys

data = open("day5/example")
seed_raw = list(map(int,data.readline().split(":")[-1].split()))
seeds = [range(seed_raw[x],seed_raw[x]+seed_raw[x+1]) for x in range(0,len(seed_raw),2)]

mapping = {}
locations = []

def split_n_strip(x):
  return x.split(":")[0].strip("\n").split()[0]

"""Create mappings"""
temp_map = [ x.split(":") for x in "".join(data.readlines()).split("\n\n")]

for j in temp_map:
  key, values = (split_n_strip(j[0]), [list(map(int, x.split())) for x in j[1].split("\n") if not len(x) == 0])
  mapping[key] = values

def s_to_d(key :str, n: int) -> int:
  for map in mapping[key]:
    source, dest, offset = (map[1],map[0], map[2])
    if n>=source and n<=source+offset:
      return n - source + dest

  return n

def map_seeds(seed_range: int) -> None:
  location = 999
  for seed in seed_range:
    x = s_to_d("seed-to-soil",seed)
    x = s_to_d("soil-to-fertilizer",x)
    x = s_to_d("fertilizer-to-water",x)
    x = s_to_d("water-to-light",x)
    x = s_to_d("light-to-temperature",x)
    x = s_to_d("temperature-to-humidity",x)
    x = s_to_d("humidity-to-location",x)

    if x < location:
      location=x

  locations.append(location)

"""Run each range in separate thread"""
threads = []
for seed_range in seeds:
  x = threading.Thread(target=map_seeds, args=(seed_range,))
  threads.append(x)
  print("[%s] Checking range with %s seeds"% (x.name, len(seed_range)))
  x.start()

"""Wait for completion"""
for index, x in enumerate(threads):
  x.join()
  print("[%s] finished"% (x.name))

print(min(locations))