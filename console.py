#!/usr/bin/python
"""
console
"""
import cmd
import re
from shlex import split
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """
    prompt = "(hbnb)"

    valid_cls = ["BaseModel", "User",
                 "Place", "State", "City",
                 "Amenity", "Review"]

    def do_create(self, arg):
        """Creates a new instance of a class"""
        arg_list = split(arg)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_cls:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg_list[0] + "()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints a string representation of an instance.

        Args:
            arg(arg): to enter with command <class name> <id>
            Example: 'show User 1234-1234-1234'

        """
        arg_list = split(arg)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_cls:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_list = storage.all()
            obj_cls = arg_list[0]
            obj_id = arg_list[1]
            key = "{}.{}".format(obj_cls, obj_id)

            if key in obj_list:
                print(obj_list[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        arg_list = split(arg)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_cls:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_list = storage.all()
            obj_cls = arg_list[0]
            obj_id = arg_list[1]
            key = "{}.{}".format(obj_cls, obj_id)

            if key in obj_list:
                del obj_list[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        arg_list = split(arg)
        obj_list = storage.all()
        arg_obj = []
        if len(arg_list) > 0:
            if arg_list[0] not in self.valid_cls:
                print("** class doesn't exist **")
            else:
                for key in obj_list.keys():
                    key_cls = key.split(".")[0]
                    if key_cls == arg_list[0]:
                        arg_obj.append(str(obj_list[key]))

        else:
            for value in obj_list.values():
                arg_obj.append(str(value))

        if len(arg_obj) > 0:
            print(arg_obj)

    def do_update(self, arg):
        """Update an instance based on the class name,
            id, attribute & value
        """
        arg_list = split(arg)

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.valid_cls:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            obj_list = storage.all()
            obj_cls = arg_list[0]
            obj_id = arg_list[1]
            key = "{}.{}".format(obj_cls, obj_id)

            if key not in obj_list:
                print("** no instance found **")
            elif len(arg_list) < 3:
                print("** attribute name missing **")
            elif len(arg_list) < 4:
                print("** value missing **")
            else:
                obj = obj_list[key]
                attr_name = arg_list[2]
                attr_value = arg_list[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def default(self, arg):
        arg_list = arg.split(".")
        class_name = arg_list[0]
        command = arg_list[1].split("(")[0]
        method = command

        xtra_args = command[1].split(")")[0]

        method_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "update": self.do_update,
            "destory": self.do_destroy,
            "count": self.do_count,
        }

        if method in method_dict.keys():
            return method_dict[method]("{} {}".format(class_name,
                                                      xtra_args))
        print("*** unknown syntax: {}".format(arg))
        return False
    
    def do_count(self, arg):
        """Count based on the class name"""
        obj_list = storage.all()
        arg_list = split(arg)

        if arg:
            class_name = arg_list[0]

        count = 0
        if arg_list:
            if class_name in self.valid_cls:
                for obj in obj_list.values():
                    if obj.__class__.__name__ == class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

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
