"""
............................
: Advent of Code Day Seven :
:..........................:

This program solves day seven 
of adventofcode.com
"""

__author__ = '@mamamia96'

from dataclasses import dataclass


@dataclass
class FileStructure():
    root: 'Folder'
    folders: list
    
    def add_folder(self, folder: 'Folder'):
        self.folders.append(folder)

    def filter_folders(self, threshold: int) -> list:
        return [folder for folder in self.folders if folder.size <= threshold]
    
    def make_space(self, space_needed: int) -> list:
        # this function takes in a number of bytes and return a sorted 
        # list of all folders that have size less than or equal to space_needed
        p_folders = [folder for folder in self.folders if folder.size >= space_needed]
        p_folders.sort()
        return p_folders
    
    def get_size(self):
        folder_sum = 0
        for folder in self.folders:
            folder_sum += folder.size
        return folder_sum


@dataclass
class File():
    _name: int
    _size: int
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        self._name = new_name
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size: int):
        self._size = new_size
    

@dataclass
class Folder():
    files: list
    folders: list
    parent_folder: 'Folder'
    
    #property attributes
    _name: str
    _size: int = 0
    
    def __lt__(self, other: 'Folder'):
        # less than overload so we can sort a list of Folders
        return self._size < other.size
        
    @property
    def name(self) -> str:
        return self._name

    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, new_size: int):
        self._size = new_size
    
    def add_file(self, file: File):
        self.files.append(file)
        
        file_sz = file.size
        current_folder = self
        
        while True:
            current_folder.size = current_folder.size + file_sz
            if current_folder.parent_folder == None: break
            current_folder = current_folder.parent_folder
    
    def add_folder(self, folder: 'Folder'):
        self.folders.append(folder)

    
    def show_files(self):
        for f in self.files:
            print(f'-{f.name}: {f.size}\n')
            
    def show_folders(self):
        for folder in self.folders:
            print(f'-{folder.name} : {folder.size}\n')

    def get_folder(self, folder_name: str) -> 'Folder':
        for folder in self.folders:
            if folder.name == folder_name:
                return folder
        return None

    def get_info(self) -> list:
        return [self._name, self._size, self.parent_folder.name, self.parent_folder.size]

    def get_file(self, file_name: str) -> File:
        for file in self.files:
            if file.name == file_name:
                return file
        return None

    def show_directory(self):
        print(f'=={self._name}==')
        self.show_folders()
        self.show_files()

def make_instructions(file_lines: list) -> list:
    # takes in a list of strings and returns a list of instructions
    instructions = []
    for i in range(len(file_lines)):
        instructions.append(file_lines[i].strip('\n'))
        instructions[i] = instructions[i].split(' ')
    
    return instructions
        
def execute_instructions(instruct: list) -> FileStructure:
    
    #outermost folder is always "\"
    origin_folder = Folder([], [], None, '\\', 0)
    
    #container class for tree of folders/files
    file_struct = FileStructure(origin_folder, [])
    active_folder = file_struct.root
    
    for i in range(1,len(instruct)):
        command = instruct[i]
        
        #NOTE: we don't need to check if it's a dir command
        #anything that doesn't start with $ is appending to our active_folder
        if command[0] == '$':
            '''terminal command'''
            if command[1] == 'cd':
                if command[2] == '..':
                    active_folder = active_folder.parent_folder
                    continue

                #going down a directory
                next_folder = active_folder.get_folder(command[2])
                if not next_folder:
                    next_folder = Folder([], [], active_folder, command[2], 0)
                    file_struct.add_folder(next_folder)

                active_folder.add_folder(next_folder)
                active_folder = next_folder
                
        else:
        #NOTE: here we are just appending files OR folders to active_folder
            if command[0] == 'dir':
                #folder
                next_folder = active_folder.get_folder(command[1])

                if not next_folder:
                    next_folder = Folder([], [], active_folder, command[1], 0)
                    file_struct.add_folder(next_folder)
                active_folder.add_folder(next_folder)
            else:
                #file
                next_file = active_folder.get_file(command[1])
                
                if not next_file:
                    next_file = File(command[1],int(command[0]))
                active_folder.add_file(next_file)                

    return file_struct
    


def main():
    file_lines = ''
    with open('input.txt', 'r') as f:
        file_lines = f.readlines()
    fs = execute_instructions(make_instructions(file_lines))
    
    #part one answer
    valid_folders = fs.filter_folders(100000)
    
    valid_sum = 0
    for folder in valid_folders:
        valid_sum += folder.size
    
    print(f'==PART ONE==\n{valid_sum}\n\n')
    
    
    #part two
    system_space = 70000000
    needed_space = 30000000
    
    #since root folder contains everything else our 
    #file structure's total size is just the root folder's size
    used_space = fs.root.size
    available_space = system_space - used_space
    print(f'==PART TWO==')
    print(fs.make_space(needed_space - available_space)[0].size)
  
if __name__ == '__main__':
    main()