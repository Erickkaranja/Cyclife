#!/usr/bin/python3
"""a simple cmd which will be used by admin to add products,
   update products and delete products.
"""
import sys

import cmd2

from models import storage
from models.bicycle import Bicycle
from models.cart import Cart
from models.order import Orders
from models.review import Review
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

create_cart_parser = create_subparsers.add_parser("cart", help="Create cart")
create_cart_parser.add_argument("-u", "--user_id", help="User id")
create_cart_parser.add_argument("-b", "--bicycle_id", help="Bicycle id")
create_cart_parser.add_argument("-q", "--quantity", help="Bicycle quantity")

create_order_parser = create_subparsers.add_parser(
    "order", help="Create order"
)
create_order_parser.add_argument("-s", "--order_status", help="Order status")
create_order_parser.add_argument("-p", "--total_price", help="Total proce")
create_order_parser.add_argument("-u", "--user_id", help="User id")
create_order_parser.add_argument("-b", "--bicycle_id", help="Bicycle id")

show_parser = base_subparsers.add_parser("show", help="show objects")
show_subparsers = show_parser.add_subparsers(
    title="subcommands", help="subcommand help"
)
show_all_parser = show_subparsers.add_parser("all", help="show all objects")
show_users_parser = show_subparsers.add_parser("users", help="show users")
show_bicycles_parser = show_subparsers.add_parser(
    "bicycles", help="show bicycles"
)
show_user_parser = show_subparsers.add_parser("user", help="show users")
show_user_parser.add_argument("-u", "--user_id", help="User id")
show_user_parser.add_argument(
    "-c", "--show_carts", action="store_true", help="Show user carts"
)
show_user_parser.add_argument(
    "-o", "--show_orders", action="store_true", help="Show user orders"
)
show_user_parser.add_argument(
    "-r", "--show_reviews", action="store_true", help="Show user reviews"
)
update_parser = base_subparsers.add_parser("update", help="update objects")
update_subparsers = update_parser.add_subparsers(
    title="subcommands", help="subcommand help"
)
update_user_parser = update_subparsers.add_parser("user", help="update user")
update_user_parser.add_argument(
    "-u", "--user_id", help="User id", required=True)
update_user_parser.add_argument("-f", "--first_name", help="user first name")
update_user_parser.add_argument("-l", "--last_name", help="user last name")
update_user_parser.add_argument("-e", "--email", help="user email")
update_user_parser.add_argument("-p", "--password", help="user password")

update_bicycle_parser = update_subparsers.add_parser(
    "bicycle", help="update bicycle"
)
update_bicycle_parser.add_argument(
    "-i", "--bicycle_id", help="bicycle id", required=True)
update_bicycle_parser.add_argument("-m", "--model", help="bicycle model")
update_bicycle_parser.add_argument("-b", "--brand", help="bicycle brand")
update_bicycle_parser.add_argument("-p", "--price", help="bicycle price")
update_bicycle_parser.add_argument(
    "-d", "--description", help="bicycle description"
)


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
        new_user = User()
        [setattr(new_user, k, v) for k, v in new_dict.items()]
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
        new_bicycle = Bicycle()
        [setattr(new_bicycle, k, v) for k, v in new_dict.items()]
        print(new_bicycle.id)
        new_bicycle.save()

    create_bicycle_parser.set_defaults(func=create_bicycle)

    def create_cart(self, args):
        """
        Create new instance of cart object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["user_id", "bicycle_id", "quantity"]
        }
        new_cart = Cart()
        print(new_cart.id)
        [setattr(new_cart, k, v) for k, v in new_dict.items()]
        new_cart.save()

    create_cart_parser.set_defaults(func=create_cart)

    def create_order(self, args):
        """
        Create new instance of order object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["order_status", "total_price", "user_id", "bicycle_id"]
        }
        new_order = Orders()
        [setattr(new_order, k, v) for k, v in new_dict.items()]
        print(new_order.id)
        new_order.save()

    create_order_parser.set_defaults(func=create_order)

    def create_review(self, args):
        """
        Create new instance of review object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["user_id", "bicycle_id", "rating", "text"]
        }
        new_review = Review()
        [setattr(new_review, k, v) for k, v in new_dict.items()]
        print(new_review.id)
        new_review.save()

    create_order_parser.set_defaults(func=create_order)

    def show_all(self, args):
        """
        Show all objects in database
        """
        all_objects = storage.all()
        print([obj.to_dict() for _, obj in all_objects.items()])

    show_all_parser.set_defaults(func=show_all)

    def show_users(self, args):
        """
        Show user instances
        """
        users = storage.all(cls=User)
        print([obj.to_dict() for _, obj in users.items()])

    show_users_parser.set_defaults(func=show_users)

    def show_user(sefl, args):
        user = storage.get(cls=User, id=args.user_id)
        # print(user)
        if args.show_carts:
            print([obj.to_dict() for obj in user.carts])
        elif args.show_orders:
            print([obj.to_dict() for obj in user.orders])
        elif args.show_reviews:
            print([obj.to_dict() for obj in user.reviews])
        else:
            user_info = {
                user.id: {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "reviews": [obj.to_dict() for obj in user.reviews],
                    "orders": [obj.to_dict() for obj in user.orders],
                    "carts": [obj.to_dict() for obj in user.carts],
                }
            }
            print(user_info)

    show_user_parser.set_defaults(func=show_user)

    def show_bicycles(self, args):
        """
        Show bicycle instances
        """
        bicycles = storage.all(cls=Bicycle)
        print([obj.to_dict() for _, obj in bicycles.items()])

    show_bicycles_parser.set_defaults(func=show_bicycles)

    def update_user(self, args):
        """
        Update existing instance of user object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["first_name", "last_name", "email", "password"]
            and v is not None
        }
        user = storage.get(User, args.user_id)
        [setattr(user, k, v) for k, v in new_dict.items()]
        user.save()

    update_user_parser.set_defaults(func=update_user)

    def update_bicycle(self, args):
        """
        update new instance of bicycle object
        """
        new_dict = {
            k: v
            for k, v in dict(args._get_kwargs()).items()
            if k in ["model", "brand", "price", "description", "image"]
            if v is not None
        }
        bicycle = storage.get(Bicycle, id)
        [setattr(bicycle, k, v) for k, v in new_dict.items()]
        print(bicycle.id)
        bicycle.save()

    update_bicycle_parser.set_defaults(func=update_bicycle)

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

    @cmd2.with_argparser(show_parser)
    def do_show(self, args):
        """
        Add command help
        """
        func = getattr(args, "func", None)
        if func is not None:
            func(self, args)
        else:
            self.do_help("base")

    @cmd2.with_argparser(update_parser)
    def do_update(self, args):
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
