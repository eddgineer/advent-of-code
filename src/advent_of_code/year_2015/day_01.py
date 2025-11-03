# https://adventofcode.com/2015/day/1

from itertools import accumulate

from advent_of_code.utils.file import read_file_into_array

# get the data file as a list of characters
file_path = "src/advent_of_code/data/year_2015/day_01.data"
lines = read_file_into_array(file_path)
chars = [char for line in lines for char in line]

# convert characters into numbers 1 or -1
values = [1 if c == '(' else -1 for c in chars]

# we can just sum the values 
def part_1():    
    return sum(values)

# we iterate and accumulate until we reach -1 while keeping index
def part_2():
    for i, total in enumerate(accumulate(values, initial=0)):
        if total == -1:
            return i
