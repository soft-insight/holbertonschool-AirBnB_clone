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
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif f"{args[0] + '.' + args[1]}" not in objs:
            print("** no instance found **")
        else:
            print(objs[f"{args[0] + '.' + args[1]}" ])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        args = line.split()
        objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
        else:
            del objs[f"{args[0]}.{args[1]}"]
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

    def do_update(self, line):
        """ Updates an instance based on the class
            name and id by adding or updating attribute
            (save the change into the JSON file).
        """
        args = line.split()
        objs = storage.all()
        key = args[0] + '.' + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in objs.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = objs[key]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objs[key]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
