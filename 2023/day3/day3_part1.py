import re

data = open("day3/input").readlines()

data_map = [[y for y in x] for x in data]

"""Find all symbols"""
symbols = []
for row in range(len(data_map)):
  symbols.extend(re.findall('[^.^\d^\\n]+', "".join(data_map[row])))

symbols = list(set(symbols))

def check_adjacent_chars(x_pos, y_pos: int) -> bool:
  for x in [-1,0,1]:
    for y in [-1,0,1]:
      try:
        if data_map[x_pos + x][y_pos + y] in symbols:
          return True
      except IndexError:
        pass
  return False

# Part 1
sum=0
part_no, part_found = None, False

"""Loop rows in map"""
for row in range(len(data_map)):

  """Look up whole numbers in the row"""
  numbers_in_row = re.findall('[\d]+', "".join(data_map[row]))

  """Skip to next row unless we found numbers"""
  if not numbers_in_row:
    continue

  """For each number in our list, check adjacent positions"""
  for col in range(len(data_map[row])):
    if data_map[row][col].isdigit():
      
      """Pop number from list"""
      if not part_no:
        part_no = int(numbers_in_row.pop(0))
      
      """Must check all surrounding chars for this position"""
      if check_adjacent_chars(row, col) and not part_found:
        """Mark as found so we dont check same part_no again"""
        part_found = True
        sum+=part_no
    else:
      """Reset and look for next part number"""
      part_no, part_found = None, False

print("Summary: %s"% sum)
