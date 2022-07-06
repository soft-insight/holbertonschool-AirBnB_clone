#!/usr/bin/python3
# AirBnB console


import cmd


class HBNBCommand(cmd.Cmd):
    """ Command line interface for AirBnB project """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ method to exit from the console """
        exit()

    def do_EOF(self, line):
        """ close the AirBnB console """
        return True
    #     # return super().postloop()

    def emptyline(self):
        """ called when empty line is entered.
            If this method is not overridden,
            it repeats the last nonempty command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
