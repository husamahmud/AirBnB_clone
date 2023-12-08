#!/usr/bin/python3
"""Module for the HBNBCommand class and command interpreter"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '
    __classes = ["BaseModel"]

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class>
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
        storage.new(inst)
        print(inst.id)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        storage.delete(key)
        storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        Usage: show <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
