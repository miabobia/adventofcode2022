"""
..........................
: Advent of Code Day Four:
:........................:

This program solves day four of 
adventofcode.com's day four problem
part one and two

"""

import re


class Elf:

    
    def __init__(self, low_bound, upper_bound):
        self.low_bound = low_bound
        self.upper_bound = upper_bound
        
    def contains_elf(self, other_elf):
        #checks if self.elf contains another elf's range
        other_bounds = other_elf.get_bounds()
        return(self.low_bound <= other_bounds[0] and self.upper_bound >= other_bounds[1])
    
    def overlap_elf(self, other_elf):
        #checks if self.elf has any overlapping value with another Elf
        other_range = other_elf.get_range_vals()
        self_range = self.get_range_vals()
        for j in range(len(self_range)):
            if self_range[j] in other_range: return True
        
        return False

    def get_bounds(self):
        return (self.low_bound, self.upper_bound)

    def get_range_vals(self):
        #gets all values between lower and upper bounds inclusively
        return [i for i in range(self.low_bound,self.upper_bound+1)]

def main():
    file_lines = ''
    with open('input.txt','r') as f:
        file_lines = f.readlines()

    elves = []
    contained_count = 0
    overlap_count = 0

    for j in range(len(file_lines)):

        #using regex to get all relevant information from each line
        line = re.findall('[0-9]+', file_lines[j])

        #each line has two elve's information so we construct two Elf objects
        elves.append(Elf(int(line[0]), int(line[1])))
        elves.append(Elf(int(line[2]), int(line[3])))

        elf_one = elves[len(elves)-1]
        elf_two = elves[len(elves)-2]

        #checks for part one
        if elf_one.contains_elf(elf_two) \
        or elf_two.contains_elf(elf_one):
            contained_count += 1  
        
        #checks for part two
        if elf_one.overlap_elf(elf_two): overlap_count += 1

    print(f'==PART=ONE==\ncontained count {contained_count}')
    print(f'==PART=TWO==\noverlap count {overlap_count}')

if __name__ == '__main__':
    main()