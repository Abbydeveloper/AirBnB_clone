#!/usr/bin/python3
"""Define HBNB console"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Define the HBNB command interpreter"""

    prompt = "(hbnb) "
    __classes = {
            "BaseModel"
            }

    def emptyline(self):
        """"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signals exit"""
        print("")
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
