# class representing the .tex file for a tree

class tree_tex():
    def __init__(self, name):
        self.name = name
        self.images = []       # list of images included
        self.tex = ""          # contents of .tex file
        self.last_edited = get_time #
        self.last_compiled = None

    def set_images(image_list):
        self.images = image_list

    def read_tex(self):
        # TODO read the tex file and get the contents
        # as a list of strings

    def mark_compiled(self):
        # updates the last compiled time

    def out_of_date(self):
        # returns if last_edit time > last_compiled time
        # indicating the file is out of date

