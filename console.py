#!/usr/bin/python3
"""a simple cmd which will be used by admin to add products,
   update products and delete products.
"""
import cmd
from models.bicycle import Bicycle


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

    def do_create(self, args):
        """create's a new instance of our product bicycle.
           usage: create bicycle <key1=value1> <key2=value2> <key3=value3> ...
           prints id after new instance is created.
        """
        new_dict = {}
        my_list = args.split(' ')
        for arg in my_list[1:]:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if '_' in value:
                    value = value.replace('_', ' ')
                elif '_' not in value:
                    value = str(value)
                else:
                    value = int(value)
            new_dict[key] = value
        obj = Bicycle(**new_dict)
        print(new_dict)
        print(type(new_dict))
        print(obj.id)
        obj.save()

if __name__ == '__main__':
    CyclifeCommand().cmdloop()
