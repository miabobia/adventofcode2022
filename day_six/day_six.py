"""
..........................
: Advent of Code Day Six :
:........................:

This program solves day six of 
adventofcode.com's day six problem
part one and two

"""
__author__ = '@mamamia96'


class StreamAnalyzer:
    
    def __init__(self, stream: str, compare_len: int):
        self.compare_len = compare_len
        self.compare_list = [stream[i] for i in range(compare_len)]

    def shift_left(self) -> list:
        shifted_list = [self.compare_list[i+1] for i in range(len(self.compare_list)-1)]
        return shifted_list
    
    def is_unique(self, u_list: list) -> bool:
        for j in range(len(u_list)):
            tmp_list = [item for item in u_list]
            tmp_list.remove(u_list[j])
            if u_list[j] in tmp_list: return False
        return True
    
    def get_compare_list(self) -> list:
        return self.compare_list
    
    def set_compare_list(self, comp_list: list):
        self.compare_list = comp_list
        
    def append_compare_list(self, item: str):
        self.compare_list.append(item)

def main(unique_len: int):
    stream: str = ''
    with open('input.txt', 'r') as f:
        stream = f.read()

    stream_a = StreamAnalyzer(stream, unique_len)

    for i in range(len(stream) - (unique_len - 1)):
        if stream_a.is_unique(stream_a.get_compare_list()):
            print(f'packet starts at: {i + unique_len}')
            break
        
        stream_a.set_compare_list(stream_a.shift_left())
        stream_a.append_compare_list(stream[i + unique_len])


if __name__ == '__main__':
    packet_len = int(input('how long is your packet identifying string?: '))
    main(packet_len)

