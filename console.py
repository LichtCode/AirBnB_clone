#!/usr/bin/python
"""
console
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits console with ctrl+d"""
        print()
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
