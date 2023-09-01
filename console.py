#!/usr/bin/python3
"""a simple cmd which will be used by admin to add products,
   update products and delete products.
"""
import cmd
from models.bicycle import Bicycle

classes = {"Bicycle": Bicycle}

class CyclifeCommand(cmd.Cmd):
    """Cyclife console."""
    prompt = '(Cyclife) '

    def do_EOF(self, arg):
        """exit console."""
        return True

    def emptyline(self):
        """overrite empty line method."""
        return False

    def do_quit(self, arg):
        """quit command to exit the console."""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()


if __name__ == '__main__':
    CyclifeCommand().cmdloop()
