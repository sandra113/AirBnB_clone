#!/usr/bin/python3
"""AirBnB clone"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """AirBnB console"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """print and empty line"""
        return

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
