# trees.py
#
# scripts for manipulating tex files and calling methods that manipulate
# the tree_class.


import os
import argparse
import tree_tex
import sys

HOME = "./../"       # root directory for the project 


def initialize(path):
    '''searches through all tree directories and initializes new tex files
    for new trees'''


def comp_tex(path, mode):
    '''calls methods to compile tex files
    input: path - tree group to compile
           mode - "all" to recompile all files or
                  "new" to only recompile files that have been changed'''

def update(path):
   '''updates tex files in a given path
   input: path - tree group to update'''



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some trees.')
    
    parser.add_argument('command',
                        help='an integer for the accumulator')
   
    parser.add_argument('--path',
                        help='path to trees to parse relative to
                              /nimble-arborist/')
  
    parser.add_argument('--comp_mode',
                         default='all_trees',
                         help='whether to compile all tex files or only
                               newly modify files')

    args = parser.parse_args()
    
    if args.command == "init":
        initialize(args.path)

    elif args.command == "compile":
        comp_tex(args.path, args.comp_mode)

    elif args.command == "update":
        update(args.path)

    else:
        print("Command '%s' not recognized; must be one\n of: "\
               %(args.command), str(command_list))

