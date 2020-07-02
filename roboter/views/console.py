import os
import string

import termcolor


def get_template_dir_path():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, "templates")
        return template_dir_path
    
    
def find_template(temp_file):
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    return temp_file_path
    

def get_template(template_file_path, color=None):
    template = find_template(template_file_path)
    with open(template, "r", encoding="utf=8") as template_file:
        contents = template_file.read()
        contents = termcolor.colored(contents, color)
        return string.Template(contents)