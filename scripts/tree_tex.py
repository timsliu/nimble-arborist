# class representing the .tex file for a tree

class tree_tex():
    def __init__(self, name):
        self.name = name
        self.images = []            # list of images included
        self.tex = ""               # contents of .tex file
        self.last_edited = get_time #
        self.last_compiled = None
        self.has_url = False       # link to Stanford tree encyclopedia
        self.locations = []

        self.read_template()        # read contents from template tex
    
    def read_template(self):
        '''read the template tex file'''

    def read_tex(self):
        # TODO read the tex file and get the contents
        # as a list of strings

    def update_tex(self):
        '''updates the tex field of this object; does write out
        the changes to the tex file'''

        # read in the tex if there is one; none indicates new file

        # update images

        # update link

        # update locations

        # check that name still matches


    def write_tex(self):
        '''writes out the tex field to a tex file'''

        # archive the previous tex
        # write to a new tex file
        # update the last_edited date

        self.mark_edited()

    def mark_edited(self):
        '''mark that the tex file has been edited'''
    
    def compile_tex(self):
        '''compile the tex file'''

        self.mark_compiled()

    def mark_compiled(self):
        # updates the last compiled time

    def out_of_date(self):
        # returns if last_edit time > last_compiled time
        # indicating the file is out of date

