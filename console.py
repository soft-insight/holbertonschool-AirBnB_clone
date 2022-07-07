#!/usr/bin/python3
""" Class for Command promt. """


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "
    class_check = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exit command to exit the program print()\n"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if not args:
            print("** class name missing **")
        elif args in HBNBCommand.class_check:

            lists = args.split()
            obj = eval("{}()".format(lists[0]))
            obj.save()
            print(obj.id)
            storage.reload()

        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance based on
        the class name.
        """
        args = args.split()
        print(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key in all_objs:
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ shouldn’t execute anything. """

        if not args:

            obj_dict = storage.all()
            obj_list = []
            for key in obj_dict.keys():
                obj_list.append(str(obj_dict[key]))

            if len(obj_list) != 0:
                print(obj_list)
        else:
            args = args.split()
            if args[0] in HBNBCommand.class_check:

                obj_list = []
                obj_dict = storage.all()
                for key in obj_dict:
                    name = key.split('.')
                    if name[0] == args[0]:
                        obj_list.append(str(obj_dict[key]))

                if len(obj_list) != 0:
                    print(obj_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """ shouldn’t execute anything. """

        args = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        new_args2 = str(args[2]).strip("\"':")
        new_args3 = str(args[3]).strip("\"':")
        if new_args3.isdigit():
            new_args3 = int(new_args3)

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            name = obj_id.split('.')
            if name[1] == args[1]:

                setattr(all_objs[obj_id], new_args2, new_args3)
                storage.save()
                return
        print("** no instance found **")

    def count(self, args):
        """ Count the number of instances of a class give ."""
        counter = 0
        lists = args.split()

        if lists[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        for key in objects:
            name = key.split('.')
            if name[0] == lists[0]:
                counter += 1
        print(counter)

    def format_dicti(self, args):
        """ Formats the argument with dictionary
        and return a listof command.
        """
        new_list = []
        new_list.append(args[0])

        try:
            my_dict = eval(args[1][args[1].find('{'): args[1].find('}') + 1])
        except Exception:
            my_dict = None

        if type(my_dict) is dict:

            new_str = args[1][args[1].find('(') + 1: args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)

        return new_list

    def format_input(self, args):
        """ Formats the argument and return a string of command."""

        new_list = []
        if args[1].find('{') != -1:
            new_list = self.format_dicti(args)
            return new_list
        else:
            new_list = []
            new_list.append(args[0])
            new_str = args[1][args[1].find('(') + 2: args[1].find(',') - 1]
            new_str += args[1][args[1].find(','): args[1].find(')') - 0]
            new_list.append(" ".join(new_str.split(", ")))

        return " ".join(i for i in new_list)

    def default(self, args):
        """ Retrieve all instances of a class """
        lists = args.split('.')

        if len(lists) >= 2:

            if lists[1] == "all()":
                self.do_all(lists[0])
                return

            if lists[1] == "count()":
                self.count(lists[0])
                return

            if lists[1][:4] == "show":
                self.do_show(self.format_input(lists))
                return

            if lists[1][:7] == "destroy":
                self.do_destroy(self.format_input(lists))
                return

            elif lists[1][:6] == "update":
                args = self.format_input(lists)

                if type(args) is list:

                    obj = storage.all()
                    key = "{} {}".format(args[0], args[1])
                    for k in args[2]:
                        self.do_update(key + '"{}" "{}"'.format(k, args[2][k]))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
