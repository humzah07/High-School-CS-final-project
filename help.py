def long_line():
    """ This creates a line between the output to seperate code """
    print("------------------------------------------------------------------")


def help():
    print("""
                                    HELP

        Some basic rules of the program:

        Enter the letter associated with the option in the menu to
        access that part of the program.
        For example: to access "a: create a file" in the menu,
        you need to enter the letter "a" when asked
        ,"What would you like to do today",
        and it will then take you to that part of the program.

        When asked a question in the program, enter "yes" or "no"
        for the program to process the request

        Create a file first in order to access other features
        such as editing or viewing a File

        You can only write one line when creating a File.
        To add more, go to "edit a file" to add one line at a time.

        You can not have two files with the same name.
        New file created with the same name will overwrite the existing
        file's contents.

        When entering a file name, the name should be matching the
        letter case of the file.""")
    long_line()
