import re
import math

data = open("day3/input").readlines()
data_map = [[y for y in x] for x in data]

# Part 2
"""Store position of all numbers in a map"""
all_numbers = {}
for row in range(len(data_map)):
  all_numbers[row] = [x for x in re.finditer('[\d]+', "".join(data_map[row]))]

def check_position_return_matching_number(x,y):
  for row in all_numbers.keys():
    for number in all_numbers[row]:
      start, stop = number.span()

      if x == row and y in range(start, stop):
        return number
      
def check_adjacent_numbers(x_pos, y_pos: int) -> list:
  matching_nums = []
  for x in [-1,0,1]:
    for y in [-1,0,1]:
      _x = x_pos + x
      _y = y_pos + y
      if _x >= 0 and _y >= 0:
        if str(data_map[_x][_y]).isdigit():
          if match := check_position_return_matching_number(_x,_y):
            if not match in matching_nums:
              matching_nums.append(match)

  return matching_nums


sum=0

for row in range(len(data_map)):
  """Locate all gears in the row"""
  print("Checking row %s"% row)
  for gear in (re.finditer('[\*]+', "".join(data_map[row]))):
    """Check surrounding postions"""
    matching_gears = check_adjacent_numbers(row,gear.start())

    if(len(matching_gears) == 2):
      sum+=math.prod(int(x.group()) for x in matching_gears)


print("Sum: %s"% sum)