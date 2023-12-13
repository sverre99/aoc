import re

def parse_line(line: str) -> str:
  all_nums = [x for x in line if x.isdigit()]

  if len(all_nums) == 1:
    return "%s%s"% (all_nums[0],all_nums[0])
    
  if len(all_nums) > 1:
    return "%s%s"% (all_nums[0],all_nums[-1])

data = open("day1/input").readlines()
sum = 0

for line in data:
  sum+=int(parse_line(line))

print("Summary of all calibration values: ", int(sum))

sum = 0

# Part 2

for line in data:
  sum+=int(parse_line(line.replace("one", "one1one")\
  .replace("two", "two2two")\
  .replace("three", "three3three")\
  .replace("four", "four4four")\
  .replace("five", "five5five")\
  .replace("six", "six6six")\
  .replace("seven", "seven7seven")\
  .replace("eight", "eight8eight")\
  .replace("nine", "nine9nine")))

print("Summary of all calibration values: ", int(sum))