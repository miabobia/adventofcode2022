"""
..........................
: Advent of Code Day Five:
:........................:

This program solves day five of 
adventofcode.com's day five problem
part one and two

"""

import re

__author__ = '@mamamia96'

class Crate:
    
     
    def __init__(self, data=None):
        self.data: str = data

    def get_data(self):
        return self.data

    def set_data(self,data:str):
        self.data = data


class CrateStack(list):


    def __init__(self, crate_list: list):
        super().__init__(crate for crate in crate_list)
        
    def show_crates(self):
        for i in range(len(self)-1,-1,-1):
            print(f'[{self[i].get_data()}]')
        print()

    def push(self, crate: Crate):
        self.append(crate)
        
    def get_top_crate(self) -> Crate:
        if len(self):
            return self[len(self)-1]
        else:
            return None
    
    def multi_pop(self,n: int) -> list:
        return [self.pop() for i in range(n)]

def make_instructions(inst_str: str) -> list:
    return re.findall('[0-9]+', inst_str)

def make_crates(stack_lines: str) -> list:
    #function that parses the stack portion of the
    #input file and returns a list of crates
    crates = []
    stack_positions = []
    stack_positions_ind = 0
    
    for pos in range(len(stack_lines[len(stack_lines) - 1])):
        if stack_lines[len(stack_lines) - 1][pos].isnumeric():
            stack_positions.append(pos)
            crates.append([])

    for i in range(len(stack_lines)-1,-1,-1):
        for j in range(len(stack_lines[i])):
            
            if j == stack_positions[stack_positions_ind]:
                if stack_lines[i][j].isalpha():
                    crates[stack_positions_ind].append(Crate(stack_lines[i][j]))

                stack_positions_ind += 1
                
                if stack_positions_ind == len(stack_positions): break
        stack_positions_ind = 0
        
    return crates
#=============================

def main(part_one):
    
#====INPUT=PARSING===================================
    stack_lines: list
    file_lines      = ''
    stack_string    = ''
    instruct_string = ''
    
    crate_stacks = []

    stacks_made = False

    with open('input.txt','r') as f:
        file_lines = f.readlines()
    
    for j in range(len(file_lines)):
        if not stacks_made and file_lines[j][0].isalpha():
            stacks_made = True

        if stacks_made:
            instruct_string += file_lines[j]
        else:
            stack_string += file_lines[j]    

    stack_lines = stack_string.splitlines()
    stack_lines = stack_lines[0:len(stack_lines)-1]
#====================================================

    instructions = make_instructions(instruct_string)
    crate_list = make_crates(stack_lines)
    
    for crates in crate_list:
        crate_stacks.append(CrateStack(crates))

    for i in range(0,len(instructions), 3):
        move_amount = int(instructions[i])
        start_loc   = int(instructions[i+1]) - 1
        end_loc     = int(instructions[i+2]) - 1
        
        if part_one:
            for j in range(move_amount):
                popped_crate = crate_stacks[start_loc].pop()
                crate_stacks[end_loc].push(popped_crate)
        
        else:     
            multi_pop = crate_stacks[start_loc].multi_pop(move_amount)

            for k in range(len(multi_pop)-1, -1, -1):
                crate_stacks[end_loc].push(multi_pop[k])

    #printing out answer based on part_one parameter
    for cs in crate_stacks:
        print(cs.get_top_crate().get_data(),end='')
    print()

if __name__ == '__main__':
    main(1)