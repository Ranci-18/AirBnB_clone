#!/usr/bin/env python3
"""entry point of the command interpreter"""

import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """Interpreter class"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Command creates new instance of BaseModel
        saves it and prints its unique id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_inst = eval(class_name)()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """command prints string representation
        instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        arguments = arg.split()
        class_name = arguments[0]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        inst_id = arguments[1]
        key = "{}.{}".format(class_name, inst_id)
        py_objs = models.storage.all()

        if key in py_objs:
            instance = py_objs[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """command deletes instance based on class name and id
        also saves change to JSON file"""
        if not arg:
            print("** class name missing **")
            return
        arguments = arg.split()
        class_name = arguments[0]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(arguments) < 2:
            print("** instance id missing **")
            return
        inst_id = arguments[1]
        key = "{}.{}".format(class_name, inst_id)
        py_objects = models.storage.all()

        if key in py_objects:
            del py_objects[key]
        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """Method to check EOF"""
        return True

    def emptyline(self):
        """Method accomodates an empty line
        Enter does not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()