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
            print("** class name is missing **")
        else:
            sub_arg = arg.split(" ")
            if sub_arg[0] not in HBNBCommand.__classes:
                print("&& class doesn't exist **")
            elif len(sub_arg) < 2:
                print("** instance id missing **")
            else:
                pattern = "{}>{}".format(sub_arg[0], sub_arg[1])
                if pattern not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[pattern])

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
                    print("** not instance found **")
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
                new = [str(obj) for patter, obj in storge.all().items()
                        if type(obj).__name__ == sub_arg[0]]
                print(new)
        else:
            f_list = [str(obj) for pattern, obj in storage.all().items()]
            print(f_list)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
