#!/usr/bin/python3
"""Define HBNB console"""

import cmd
from models import storage
from models.base_model import BaseModel
import re
import json


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

    def do_create(self, arg):
        """Create new BaseModel instance"""

        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            storage.save()
            print(eval(arg)().id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            sub_arg = arg.split(" ")
            if sub_arg[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(sub_arg) < 2:
                print("** instance id missing **")
            else:
                pattern = "{}.{}".format(sub_arg[0], sub_arg[1])
                if pattern not in storage.all():
                    print("** no instance found **")
                else:
                   print(storage.all()["{}.{}".format(sub_arg[0], sub_arg[1])])

    def do_destroy(self, arg):
        """Delete an instance with class name and id"""

        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            sub_arg = arg.split(" ")
            if sub_arg[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(sub_arg) < 2:
                print("** instance id missing **")
            else:
                pattern = "{}.{}".format(sub_arg[0], sub_arg[1])
                if pattern not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[pattern]
                    storage.save()

    def do_all(self, arg):
        """Print all string representation of an instance"""

        if arg != "":
            sub_arg = arg.split(" ")
            if sub_arg[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                new = [str(obj) for patter, obj in storage.all().items()
                        if type(obj).__name__ == sub_arg[0]]
                print(new)
        else:
            f_list = [str(obj) for pattern, obj in storage.all().items()]
            print(f_list)

    def do_update(self, arg):
        """Update an instance based on the name and id"""

        if arg == "" or arg is None:
            print("** class name missing **")
            return

        reg = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(reg, arg)
        cls_name = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            pattern = "{}.{}".format(cls_name, uid)
            if pattern not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:

                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.all().__class__.__dict__.keys()                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[pattern], attribute, value)
                storage.all()[pattern].save()
               """ obj = storage.all()["{}.{}".format(arg[0], arg[1])]
                if attribute in obj.__"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
