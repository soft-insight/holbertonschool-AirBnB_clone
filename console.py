#!/usr/bin/python3
""" AirBnB console """
import cmd
from models import storage
from models.base_model import BaseModel

classes = {
        "BaseModel": BaseModel
        }


class HBNBCommand(cmd.Cmd):
    """ Command line interface for AirBnB project """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program """
        return True

    def emptyline(self):
        """ called when empty line is entered """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        if args[0] in classes:
            instance = classes[args[0]]()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of
            an instance based on the class name and id.
        """
        args = line.split()
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def destroy(self, line):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args = line.split()
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name.
        """
        args = line.split()
        store = storage.all()
        list_n = []

        if len(args) == 0:
            for a in store.values():
                list_n.append(a.__str__())
            print(list_n)

        elif args[0] in classes:
            for a in store.values():
                if a.__class__.__name__ == args[0]:
                    list_n.append(a.__str__())
            print(list_n)
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
