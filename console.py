#!/usr/bin/python3
"""Module for the HBNBCommand class and command interpreter"""

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
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '
    __classes = ["BaseModel",
                 "User",
                 "State",
                 "City",
                 "Amenity",
                 "Place",
                 "Review"]

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

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
            return
        if len(args) < 3:
            print("** instance id missing **")
            return
        class_name, inst_id = args[:2]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{inst_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return
        attr_name = args[2]
        val = eval(args[3])
        inst = storage.all()[key]
        setattr(inst, attr_name, val)
        storage.save()

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
        Prints the string representation of an instance based on the class
        name and id
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

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the
        class name
        Usage: all <class name> OR all
        """
        objects = storage.all().values()
        instances = []

        if line:
            class_name = line.split()[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            for obj in objects:
                if obj.__class__.__name__ == class_name:
                    instances.append(str(obj))
        else:
            for obj in objects:
                instances.append(str(obj))
        print(instances)

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
