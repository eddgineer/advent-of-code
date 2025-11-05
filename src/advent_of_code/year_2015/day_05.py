# https://adventofcode.com/2015/day/5

from advent_of_code.utils.file import read_file_into_array


file_path = "src/advent_of_code/data/year_2015/day_05.data"
lines = read_file_into_array(file_path)

contains_three_vowels = lambda s: sum(c in 'aeiou' for c in s) >= 3
two_letters_in_a_row = lambda s: any(s[i] == s[i+1] for i in range(len(s)-1))
does_not_contain_strings = lambda s: not any(bad in s for bad in ['ab', 'cd', 'pq', 'xy'])
pair_appears_twice = lambda s: any(s[i:i+2] in s[i+2:] for i in range(len(s)-1))
letter_repeats_with_one_between = lambda s: any(s[i] == s[i+2] for i in range(len(s)-2))

is_nice_string = lambda s: all([contains_three_vowels(s), two_letters_in_a_row(s), does_not_contain_strings(s)])
is_very_nice_string = lambda s: all([pair_appears_twice(s), letter_repeats_with_one_between(s)])

print(sum([1 for line in lines if is_nice_string(line)]))
print(sum([1 for line in lines if is_very_nice_string(line)]))
