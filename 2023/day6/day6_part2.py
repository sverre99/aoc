import math
input = open("./day6/input").readlines()
t, r = list(map(int, [x for x in [input[0].split(":")[-1].replace(" ", "").strip(), input[-1].split(":")[-1].replace(" ", "").strip()]]))
print(len([x*(t-x) for x in range(t) if x*(t-x) > r]))