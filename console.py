"""
The console module.

Contains the entry point of the command interpreter.
"""


import cmd

from models.base_model import BaseModel
from models.user import User
from models import storage


class OwlDenCommand(cmd.Cmd):
    """
    OwldenCommand class.

    Implements the command interpreter of the OwlDen project.
    """

    prompt = "(OwlDen) "
    classes_list = ['BaseModel', 'User']

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """

        classes_dict = {
            'BaseModel': BaseModel,
            'User': User
        }

        if not line:
            print("** class name missing **")
        elif line not in OwlDenCommand.classes_list:
            print("** class doesn't exist **")
        else:
            new_instance = classes_dict[line]()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """Prints the help documentation for create."""
        print(
            """
            [Usage]: create <class name>

            Creates a new instance of BaseModel, saves it (to the JSON file),
            and prints the id.

            If the class name is missing, print ** class name missing **
            If the class name doesn't exist, print ** class doesn't exist **
            """
        )

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        import shlex

        args = shlex.split(line)

        # Check if args are empty
        if len(args) < 1:
            print("** class name missing **")
            return

        # Check if instance id is present
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_data = args[:2]  # Class name > [0] and instance id > [1]

        # Now check if class name is valid
        if instance_data[0] not in OwlDenCommand.classes_list:
            print("** class doesn't exist **")
            return

        # Genrate the key to check if instance exists
        instance_key = "{}.{}".format(instance_data[0], instance_data[1])
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        # Check if attribute name is present
        if len(args) < 3:
            print("** attribute name missing **")
            return

        # Check if attribute value is present
        if len(args) < 4:
            print("** value missing **")
            return

        instance_attr_data = args[2:4]  # attribute name > [0] and value > [1]
        instance = storage.all()[instance_key]

        # Casting attribute value to the correct type
        attribute_value = None
        if hasattr(instance, instance_attr_data[0]):
            attr_type = type(getattr(instance, instance_attr_data[0]))
            attribute_value = attr_type(instance_attr_data[1])

        if attribute_value:
            setattr(instance, instance_attr_data[0], attribute_value)
        else:
            setattr(instance, instance_attr_data[0], instance_attr_data[1])

        instance.save()

    def help_update(self):
        """Prints the help documentation for update."""
        print(
            """
            [Usage]: update <class name> <id> <attr name> "<attr value>"

            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).

            If the class name is missing, print ** class name missing **
            If the class name doesn't exist, print ** class doesn't exist **
            If the id is missing, print ** instance id missing **
            If the instance of the class name doesn't exist for the id,
            print ** no instance found **
            If the attribute name is missing,
            print ** attribute name missing **
            If the value for the attribute name doesn't exist,
            print ** value missing **
            """
        )

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""

        if not line:
            print("** class name missing **")
            return

        instance_data = line.split(" ")

        # Check for instance id
        if len(instance_data) != 2:
            print("** instance id missing **")
            return

        # Check for instance name
        if instance_data[0] not in OwlDenCommand.classes_list:
            print("** class doesn't exist **")
            return

        # Generate instance key from its name and id
        instance_key = "{}.{}".format(instance_data[0], instance_data[1])

        # Try delete insatnce key if it exists
        try:
            del(storage.all()[instance_key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Prints the help documentation for destroy."""
        print(
            """
            [Usage]: destroy <class name> <id>

            Deletes an instance based on the class name and id
            (save the change into the JSON file).

            If the class name is missing, print ** class name missing **
            If the class name doesn't exist, print ** class doesn't exist **
            If the id is missing, print ** instance id missing **
            If the instance of the class name doesn't exist for the id,
            print ** no instance found **
            """
        )

    def do_show(self, line):
        """Shows Indvidual instance string representation."""
        if not line:
            print("** class name missing **")
            return

        instance_data = line.split(" ")

        # Check for instance id
        if len(instance_data) != 2:
            print("** instance id missing **")
            return

        # Check for instance name
        if instance_data[0] not in OwlDenCommand.classes_list:
            print("** class doesn't exist **")
            return

        # Generate instance key from its name and id
        instance_key = "{}.{}".format(instance_data[0], instance_data[1])

        # Try print insatnce key if it exists
        try:
            print(storage._FileStorage__objects[instance_key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Prints the help documentation for show."""
        print(
            """
            [Usage]: show <class name> <id>

            Prints the string representation of an instance based on
            the class name and id.

            If the class name is missing, print ** class name missing **
            If the class name doesn't exist, print ** class doesn't exist **
            If the id is missing, print ** instance id missing **
            If the instance of the class name doesn't exist for the id,
            print ** no instance found **
            """
        )

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        print_list = []

        if line:
            args = line.split(' ')[0]  # remove possible trailing args
            if args not in OwlDenCommand.classes_list:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """Prints the help documentation for all."""
        print(
            """
            [Usage]: all (<class name>)
            Brackets indicates optional args.

            The printed result is a list of strings.
            If the class name doesn't exist, print ** class doesn't exist **
            """
        )

    def do_quit(self, line):
        """Exit the interpreter using the quit command."""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit."""
        print(
            """
            [Usage]: quit

            Exits the program with formatting
            """
        )

    def do_EOF(self, line):
        """Exit the interpreter using the EOF Flag."""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF."""
        print(
            """
            [Usage]: ^D

            Exits the program without formatting
            """
        )

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    OwlDenCommand().cmdloop()
