#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

def parse(arg):
    """
    Parse a string of arguments and return a list of tokens
    """
    tokens = []
    while arg:
        match = re.search(r'(\{.*?\}|\[.*?\])', arg)
        if match:
            start, end = match.span()
            tokens.extend(arg[:start].split())
            tokens.append(arg[start:end])
            arg = arg[end:]
        else:
            tokens.extend(arg.split())
            breaak
    return token    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
