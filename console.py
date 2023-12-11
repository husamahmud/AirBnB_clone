#!/usr/bin/python3
"""Module for the HBNBCommand class and command interpreter"""

import cmd
import re
import ast

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

    def default(self, line):
        """
        Handles the default command-line input
        Usage for: all, show, destroy, count and update
        """
        cmds = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "create": self.do_create
        }
        match = re.search(r"(\w+)\.(.*?)\((.*?)\)", line)
        if match:
            obj_name, cmd, args = match.groups()
            if cmd == 'update':
                # update an instance based on his ID
                if "{" in args:
                    comma_idx = args.index(',')
                    obj_id = args[:comma_idx].strip()[1:-1]
                    dict_str = args[comma_idx + 1:].strip()
                    key = f"{obj_name}.{obj_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                        return
                    obj = storage.all()[key]
                    try:
                        update_dict = ast.literal_eval(dict_str)
                        for attr_name, attr_value in update_dict.items():
                            setattr(obj, attr_name, attr_value)
                            storage.save()
                    except (ValueError, SyntaxError):
                        print("** invalid dictionary format **")
                        return
                    return
                # to update an instance based on his ID with a dictionary
                splited = args.split(', ')
                obj_id = splited[0][1:-1]
                attr_name = splited[1][1:-1]
                attr_val = splited[2][1:-1]
                key = f"{obj_name}.{obj_id}"
                if len(splited) < 2:
                    print("** attribute name missing **")
                    return
                if len(splited) < 3:
                    print("** value missing **")
                    return
                if key not in storage.all():
                    print("** no instance found **")
                    return
                val = eval(f'"{attr_val}"')
                inst = storage.all()[key]
                setattr(inst, attr_name, val)
                storage.save()
                return
            if cmd in cmds:
                call = f'{obj_name} {args}'
                return cmds[cmd](call)
        print(f"*** Unknown syntax: {line}")
        return False

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        Usage: create <class name>
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

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        if len(args) < 2:
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
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
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
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

    def do_count(self, line):
        """
        Counts the number of instances of a specific class in the storage
        Usage: count <class name>
        """
        args = line.split()
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
