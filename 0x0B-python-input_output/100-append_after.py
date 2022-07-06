#!/usr/bin/python3
""" Search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """ This function inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'rw+') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) is not -1:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.writelines("".join(lines))
