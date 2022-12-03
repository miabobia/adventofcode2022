"""
.........................
: Advent of Code Day One:
:.......................:

This program solves day one of 
adventofcode.com's day one problem
part one and two

"""

__author__ = '@mamamia96'



class Elf_Calorie_Counter:


    #list of maximum elves
    max_elves: list
    
    #data to be read from file
    data:      list
    
    #list of elves. initialized with one empty elf
    elves:     list = [0]

    def __init__(self, f_input, max_elves_num):

        with open(f_input,'r') as f:
            self.data = f.read().splitlines()

        self.max_elves = [-1 for i in range(max_elves_num)]
        self.find_max_elves()

    def shift_down(self, shift_list : list, shf_ind :int) -> list:
    #shifts all elements from shf_ind, shf_ind-1, .. ,0 and shifts them down. 
    #element at 0 lost in process
        for i in range(len(shift_list)):
            if i == shf_ind: break
            shift_list[i] = shift_list[i+1]

        return shift_list

    def find_max_elves(self) -> None:
        
        for i in range(len(self.data)):
            if self.data[i]:
                #if line isn't empty we add to our current elf
                self.elves[len(self.elves)-1] += int(self.data[i])
            else:
                #iterate backwards through our max elves
                for j in range(len(self.max_elves)-1,-1,-1):
                    #our new elf has a place in our current max_elves list
                    if self.elves[len(self.elves)-1] > self.max_elves[j]:
                        #shift elves down to make room for our new elf
                        self.max_elves    = self.shift_down(self.max_elves, j)

                        #insert new elf
                        self.max_elves[j] = self.elves[len(self.elves)-1]

                        break

                self.elves.append(0)

    def get_max_elves(self) -> list:
        return self.max_elves

    def get_max_elves_sum(self) -> int:
        elf_sum = 0
        for i in range(len(self.max_elves)):
            elf_sum += self.max_elves[i]
        return elf_sum

    def get_max_elf(self) -> int:
        return self.max_elves[len(self.max_elves) - 1]

if __name__ == '__main__':
    #constructing elf calorie counter object
    elf_counter = Elf_Calorie_Counter('input.txt', 3)

    #__part_one___
    print(f'PART ONE -> {elf_counter.get_max_elf()}')

    #__part_two___
    print(f'PART TWO -> {elf_counter.get_max_elves_sum()}')
