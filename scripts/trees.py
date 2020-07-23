# trees.py
#
# scripts for manipulating tex files and calling methods that manipulate
# the tree_class.


import os
import argparse
import tree_tex
import sys

HOME = os.path.join(os.getcwd(), "..")     # root directory for the project
COMMAND_LIST = ["init", "compile", "update"]


def initialize(path):
    '''searches through all tree directories and initializes new tex files
    for new trees'''

    print("Running initialization on: %s" %(path))


def comp_tex(path, mode):
    '''calls methods to compile tex files
    input: path - tree group to compile
           mode - "all" to recompile all files or
                  "new" to only recompile files that have been changed'''
    print("Running compile on: %s with mode: %s" %(path, mode))

def update(path):
   '''updates tex files in a given path
   input: path - tree group to update'''

   print("Updating tex files in path: %s" %(path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some trees.')
    
    parser.add_argument('command',
                        help='command to run; must be in %s' %COMMAND_LIST)
   
    parser.add_argument('--path',
                        help='path to trees to parse relative to\
                              /nimble-arborist/',
                        default='/all_trees')
  
    parser.add_argument('--comp_mode',
                         default='all_trees',
                         help='whether to compile all tex files or only\
                               newly modify files')

    args = parser.parse_args()
    path = os.path.join(HOME, args.path)

    
    if args.command == "init":
        initialize(path)

    elif args.command == "compile":
        comp_tex(path, args.comp_mode)

    elif args.command == "update":
        update(path)

    else:
        print("Command '%s' not recognized; must be one\n of: "\
               %(args.command), str(COMMAND_LIST))

    print("Exiting tree...")

