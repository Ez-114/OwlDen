"""
The console module.

Contains the entry point of the command interpreter.
"""


import cmd


class OwlDenCommand(cmd.Cmd):
    """
    OwldenCommand class.

    Implements the command interpreter of the OwlDen project.
    """

    prompt = "(OwlDen) "

    def do_quit(self, line):
        """Exit the interpreter using the quit command."""
        exit()

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

    def help_quit(self):
        """Prints the help documentation for quit."""
        print(
            """
            [Usage]: quit

            Exits the program with formatting
            """
        )

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    OwlDenCommand().cmdloop()
