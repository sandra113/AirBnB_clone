#!/usr/bin/python3
import cmd
from models.base_model import BaseModel, storage
from models.engine.file_storage import FileStorage
import sys
import json
import datetime


class HBNBConsole(cmd.Cmd):
    """AirBnb Clone Console"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """quits the console"""
        return True

    def do_EOF(self, line):
        """Quits the console"""
        print()
        return True

    def do_create(self, line):
        """creates an instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """prints string representation based on class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = cmd.Cmd.parseline(self, line)
            stored_classes = my_classes()
            if args[0] not in stored_classes:
                print("** class doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            else:
                id_rep = f'{args[0]}.{args[1]}'
                data = storage.all()
                if id_rep not in data.keys():
                    print('** no instance found **')
                else:
                    print(f'{data[id_rep]}')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if not line:
            print("** class name missing **")
        else:
            args = cmd.Cmd.parseline(self, line)
            stored_classes = my_classes()
            if args[0] not in stored_classes:
                print("** class name doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            else:
                id_rep = f'{args[0]}.{args[1]}'
                data = storage.all()
                if id_rep not in data.keys():
                    print('** no instance found **')
                else:
                    storage.all().pop(id_rep)
                    storage.save()

    def do_all(self, line):
        '''prints all str representation of instances'''
        if not line:
            all_instaces = []
            for value in storage.all().values():
                all_instaces.append(value)
            print(all_instaces)
        else:
            stored_classes = my_classes()
            args = cmd.Cmd.parseline(self, line)
            if args[0] not in stored_classes:
                print("** class doesn't exist **")
            else:
                all_instaces = []
                for key, value in storage.all().items():
                    obj_key = key.split('.')
                    if args[0] == obj_key[0]:
                        all_instaces.append(value)
                print(all_instaces)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            stored_classes = my_classes()
            args = cmd.Cmd.parseline(self, line)
            if args[0] not in stored_classes:
                print("** class doesn't exist **")
            else:
                if not args[1]:
                    print("** instance id missing **")
                else:
                    my_args = args[1].split(' ')
                    id_rep = f'{args[0]}.{my_args[0]}'
                    if id_rep not in storage.all().keys():
                        print('** no instance found **')
                    else:
                        if len(my_args) == 1:
                            print("** attribute name missing")
                        elif len(my_args) == 2:
                            print("** value missing")
                        else:
                            my_data = my_update(id_rep, my_args[1], my_args[2])
                            storage.all()[id_rep] = my_data
                            storage.save()

    def help_create(self):
        """Creates a new instance"""
        print("create a new instance of BaseModel and its id when created")
        print("Usage: create BaseModel")

    def help_show(self):
        """prints the string representation of a class.
        Based on class name and id"""
        print("prints the string representation of a class.")
        print("Usage: show <class name> <id>")

    def help_update(self):
        """updates an instance"""
        print('Usage: update <class name> <id>', end=' ')
        print('<attribute name> "<attribute value>"')

    def help_quit(self):
        """Quits the hbnb console"""
        print("Quits the console")

    def emptyline(self):
        """Overwrites an empty line"""
        pass


def my_classes():
    """returns a set of available classes"""
    obj_keys = storage.all().keys()
    classes = []
    for obj_class in obj_keys:
        my_class = obj_class.split('.')
        classes.append(my_class[0])
    set_classes = set(classes)
    return set_classes


def my_update(class_id, attr_name, attr_value):
    """function to update an object's attributes."""
    data = storage.all()[class_id]
    my_rep = class_id.split('.')
    class_name = my_rep[0]
    my_id = my_rep[1]
    pref = f'[{class_name}] ({my_id}) '
    my_data = data.removeprefix(pref)
    my_dict = eval(my_data)
    my_dict[attr_name] = attr_value
    new_data = pref + str(my_dict)
    return new_data


if __name__ == '__main__':
    HBNBConsole().cmdloop()
