from advent_of_code.utils.file import read_file_into_array


file_path = "src/advent_of_code/data/year_2015/day_03.data"
lines = read_file_into_array(file_path)
chars = [char for line in lines for char in line]

notation = {
    '^': lambda x, y: (x, y + 1),
    '>': lambda x, y: (x + 1, y),
    'v': lambda x, y: (x, y - 1),
    '<': lambda x, y: (x - 1, y),
}

def part_1():
    x, y = 0, 0
    visited = {(x, y)}
    for char in chars:
        x, y = notation[char](x, y)
        visited.add((x, y))

    return len(visited)

def part_2():
    santa_steps = chars[1::2]
    robo_santa_steps = chars[::2]
    
    x, y = 0, 0
    visited = {(x, y)}
    
    for char in santa_steps:
        x, y = notation[char](x, y)
        visited.add((x, y))

    x, y = 0, 0

    for char in robo_santa_steps:
        x, y = notation[char](x, y)
        visited.add((x, y))

    return len(visited)

print(part_1())
print(part_2())
