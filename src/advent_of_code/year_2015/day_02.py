# https://adventofcode.com/2015/day/2

from advent_of_code.utils.file import read_file_into_array


file_path = "src/advent_of_code/data/year_2015/day_02.data"
dimensions = read_file_into_array(file_path)

def parse(dimensions):
    l, w, h = map(int, dimensions.split('x'))
    return l, w, h

def surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def calc_ribbon(l, w, h):
    return 2 * sum(sorted([l, w, h])[:2]) + l * w * h

assert(surface_area(*parse("2x3x4")) == 58)
assert(surface_area(*parse("1x1x10")) == 43)

part_1 = sum([surface_area(*parse(dimension)) for dimension in dimensions])
part_2 = sum([calc_ribbon(*parse(dimension)) for dimension in dimensions])

print(part_1)
print(part_2)