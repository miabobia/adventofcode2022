"""
...........................
: Advent of Code Day Three:
:.........................:

This program solves day three of 
adventofcode.com's day three problem
part one and two

"""

__author__ = '@mamamia96'


import character_priority


class RuckSack:
    #RuckSack represents items in each elve's rucksacks
    #It is also able to split itself into halves and see if the halves
    #have a common element
    
    half_one: str
    half_two: str
    data:     str

    def __init__(self, data, split=True) -> None:
        #takes in line of input file which contains rucksack contents
        self.data = data
        
        if split:
            #parse data passed in
            self.set_halves()
    
    def split_str(self, contents_str: str):
        #takes in a string and returns a tuple of each half of the string
        first_half = contents_str[0:len(contents_str)//2]
        second_half = contents_str[len(contents_str)//2:len(contents_str)]

        return(first_half, second_half)

    def set_halves(self) -> None:
        self.half_one,self.half_two = self.split_str(self.data)
        
    def get_halves(self):
        return(self.half_one,self.half_two)
    
    def get_common_item(self) -> chr:
        #using class variables we find the item that is in both
        #halves of the rucksack
        for item in self.half_one:
            if self.half_two.find(item) > -1:
                return item
    
        #if there isn't item in both rucksack we send back special character that has no
        #priority
        return '!'

    def get_data(self) -> str:
        return self.data


class ElfGroup:
#Elfgroup represents a group of elves. a group takes in RuckSack
#Objects and can identify common items

    def __init__(self, rucksacks: list):
        
        self.elves_data = []
        
        for j in range(len(rucksacks)):
            self.elves_data.append(rucksacks[j].get_data())
        

    def get_common_item(self) -> chr:
        #returns common item between all elves
        #specified in our self.elves_data
        #function assumes length of self.elves_data > 0

        common_item: chr
        item_found: bool
        first_elf_data = self.elves_data[0]
        
        for i in range(len(first_elf_data)):
            common_item = first_elf_data[i]
            item_found = True

            #look for common item in all of elves_data besides first entry
            for j in range(1,len(self.elves_data)):
                #item is not found
                if self.elves_data[j].find(common_item) < 0:
                    item_found = False

            #return the common item here to avoid unnecessary checks
            if item_found:
                return common_item
        
        #item wasn't found after search. return special character
        return '!'

if __name__ == '__main__':
    file_lines: list
    
    with open('input.txt','r') as f:
        file_lines = f.readlines()
        
    #PART ONE

    rucksacks = []
    priority_sum: int = 0

    for i in range(len(file_lines)):
        rucksacks.append(RuckSack(file_lines[i]))
        common = rucksacks[len(rucksacks)-1].get_common_item()
        priority = character_priority.get_priority(common)
        
        priority_sum += priority
    
    print(f'==PART=ONE==\ntotal sum of priorities -> {priority_sum}\n')
    
    #PART TWO
    
    group_rucksacks: list
    elf_group: ElfGroup
    group_priority_sum: int = 0
    
    for j in range(0,len(file_lines),3):

        #using list comprehension to construct a list of rucksacks for the next 3 elves
        group_rucksacks = [RuckSack(file_lines[j+i], False) for i in range(3)]

        elf_group = ElfGroup(group_rucksacks)

        common_group_item = elf_group.get_common_item()
        group_priority = character_priority.get_priority(common_group_item)
        group_priority_sum += group_priority

    print(f'==PART=TWO==\ntotal groups priority: {group_priority_sum}\n')
