#!/usr/bin/python3
"""Module for the HBNBCommand class and command interpreter"""

import cmd
import importlib
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '
    __classes = ["BaseModel"]

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <Class Name>
        """
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        inst = eval(class_name)()
        inst.save()
        print(inst.id)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self):
        """Exit the program"""
        return True

    def do_EOF(self):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
