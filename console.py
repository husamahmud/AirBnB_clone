#!/usr/bin/python3
"""Module for the HBNBCommand class and command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '

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
