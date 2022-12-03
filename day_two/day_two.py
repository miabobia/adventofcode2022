"""
.........................
: Advent of Code Day Two:
:.......................:

This program solves day two of 
adventofcode.com's day two problem
part one and two

"""

__author__ = '@mamamia96'

def shape_to_string(shape: str) -> str:

    if shape == 'A' or shape == 'X':
        return 'rock'
    elif shape == 'B' or shape == 'Y':
        return 'paper'
    else:
        return 'scissors'

def result_to_string(code: str) -> str:
    if code == 'X':
        return 'lose'
    elif code == 'Y':
        return 'draw'
    elif code == 'Z':
        return 'win'

def shape_val(shape: str) -> int:
    
    if   shape == 'rock':
        return 1
    elif shape == 'paper':
        return 2
    elif shape == 'scissors':
        return 3 

def rock_paper_scissors_part_one(p1: chr, p2: chr, rps_dict: dict) -> int:
    p1_str = shape_to_string(p1)
    p2_str = shape_to_string(p2)

    score = shape_val(p2_str)

    if p1_str == p2_str:
        return score + 3

    if rps_dict.get(p2_str).get(p1_str):
        return score + 6
    else:

        return score + 0

def rock_paper_scissors_part_two(p1: chr, p2: chr, rps_dict: dict, rps_predict_dict: dict):
    
    desired_result = result_to_string(p2)
    
    p1_shape = shape_to_string(p1)
    
    p2_shape = rps_predict_dict.get(p1_shape).get(desired_result)
    
    score = shape_val(p2_shape)
    
    if desired_result == 'draw':
        return score + 3
    elif desired_result == 'lose':
        return score + 0
    elif desired_result == 'win':
        return score + 6

def part_one(data: list) -> int:
    
    total_score = 0

    for line in file_lines:
        split_ln = line.split(' ')
    
        total_score += rock_paper_scissors_part_one(split_ln[0], split_ln[1], rps_dict)
    return total_score

def part_two(data: list) -> int:
    total_score = 0

    for line in file_lines:
        split_ln = line.split(' ')
        
        total_score += rock_paper_scissors_part_two(split_ln[0], split_ln[1],rps_dict,rps_predict_dict)
    
    return total_score

rps_dict = {
    'rock':{
        'paper':False,
        'scissors':True,
    },
    'paper':{
        'rock':True,
        'scissors':False
    },
    'scissors':{
        'rock':False,
        'paper':True
    }
}

rps_predict_dict = {
    'rock':{
        'draw':'rock',
        'win':'paper',
        'lose':'scissors'
    },
    'paper':{
        'draw':'paper',
        'win':'scissors',
        'lose':'rock'
    },
    'scissors':{
        'draw':'scissors',
        'win':'rock',
        'lose':'paper'
    }
}

file_lines = ''

with open('input.txt','r') as f:
    file_lines = f.read().splitlines()

print(f'PART ONE SCORE: {part_one(file_lines)}')

print(f'PART TWO SCORE: {part_two(file_lines)}')
