#!/usr/bin/python3
"""a simple cmd which will be used by admin to add products,
   update products and delete products.
"""
import sys

import cmd2

from models.bicycle import Bicycle
from models.user import User

base_parser = cmd2.Cmd2ArgumentParser(
    description="Cyclife CLI",
)
base_subparsers = base_parser.add_subparsers(
    title="subcommands", help="subcommand help"
)
create_parser = base_subparsers.add_parser("create", help="create object")
create_subparsers = create_parser.add_subparsers(
    title="subcommands", help="subcommand help"
)
create_user_parser = create_subparsers.add_parser("user", help="create user")
create_user_parser.add_argument("-f", "--first_name", help="user first name")
create_user_parser.add_argument("-l", "--last_name", help="user last name")
create_user_parser.add_argument("-e", "--email", help="user email")
create_user_parser.add_argument("-p", "--password", help="user password")
create_bicycle_parser = create_subparsers.add_parser(
    "bicycle", help="create bicycle"
)
create_bicycle_parser.add_argument("-m", "--model", help="bicycle model")
create_bicycle_parser.add_argument("-b", "--brand", help="bicycle brand")
create_bicycle_parser.add_argument("-p", "--price", help="bicycle price")
create_bicycle_parser.add_argument(
    "-d", "--description", help="bicycle description"
)
create_bicycle_parser.add_argument("-i", "--image", help="bicycle image url")


class CyclifeCommand(cmd2.Cmd):
    """Cyclife console."""

    prompt = "(Cyclife) "

    def emptyline(self):
        """overrite empty line method."""
        return False

    def do_exit(self, arg):
        """Exit"""
        self.poutput("\n** Exiting program, bye **")
        return True

    def do_quit(self, arg):
        """Exit"""
        self.poutput("\n** Exiting program, bye **")
        return True

    def do_EOF(self, arg):
        """
        Exit
        """
        self.poutput("\n** Exiting program, bye **")
        return True

    def postloop(self):
        self.poutput()

    def create_user(self, args):
        """
        Create new instance of user object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["first_name", "last_name", "email", "password"]
        }
        new_user = User(**new_dict)
        print(new_user.id)
        new_user.save()

    create_user_parser.set_defaults(func=create_user)

    def create_bicycle(self, args):
        """
        Create new instance of bicycle object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["model", "brand", "price", "description", "image"]
        }
        new_bicycle = Bicycle(**new_dict)
        print(new_bicycle.id)
        new_bicycle.save()

    create_bicycle_parser.set_defaults(func=create_bicycle)

    @cmd2.with_argparser(create_parser)
    def do_create(self, args):
        """
        Add command help
        """
        func = getattr(args, "func", None)
        if func is not None:
            func(self, args)
        else:
            self.do_help("base")


def main():
    cyclifecmd = CyclifeCommand()
    try:
        sys.exit(cyclifecmd.cmdloop())
    except (KeyboardInterrupt, EOFError):
        cyclifecmd.poutput("\nExiting the program\n")
    return True


if __name__ == "__main__":
    main()
