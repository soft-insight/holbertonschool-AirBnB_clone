#!/usr/bin/python3
# AirBnB console
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command line interface for AirBnB project """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program """
        print()
        return True

    def emptyline(self):
        """ called when empty line is entered.
            If this method is not overridden,
            it repeats the last nonempty command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
