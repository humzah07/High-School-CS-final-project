# Course: CS 30
# Period: 2
# Date created: 23/11/21
# Date last modified: 01/12/21
# Name: Humzah Zahid Malik
# Description: Large Scale program


import os
import help


def long_line():
    """ This creates a line between the output to seperate code """
    print("------------------------------------------------------------------")


# Creates a menu of valid actions in this program


valid_actions = ["a: create a file", "b: view a file", "c: edit a file",
                 """d: delete a file""", """e: Close the program""", """f: Help"""]


def main_menu():
    """ Prints the introduction of the program """
    print("""Hello there, and welcome to Record!

Record is a Python-based program for creating, viewing, editing, and deleting external files.

You can create a variety of files on this platform, ranging from text(.txt) files to PY(.py) files, and you can create an unlimited number of files.

Important:
Enter "f" for "Help", which will guide to the basic guidelines of the program.

   """)
    print("\n")


def intro():
    """ Prints all of the valid actions in a menu """
    print(""" Choose an action: """)
    for action in valid_actions:
        print(f" {action} ")
    input_1 = input("What would you like to do today? ")
    if input_1 == "a":
        notes_1()
    if input_1 == "b":
        note_2()
    if input_1 == "c":
        note_3()
    if input_1 == "d":
        note_4()
    if input_1 == "e":
        print(" You have closed the program ")
        quit()
    if input_1 == "f":
        help.help()
    else:
        print("invalid action")
        long_line()


def notes_1():
    """ This function creates new files """
    filename = input("What is the title of the note: ")
    file_name = filename
    character = input("What do you want to note? ")
    print("\n")
    with open(file_name, 'w') as file_object:
        file_object.write(character)
    filename_2 = open(filename, "r")
    print(file_name + ":")
    print(filename_2.read())
    print("\n")
    long_line()
    intro()


def note_2():
    """ This functions opens files in view mode """
    try:
        filename = input("Which file do you want to open?: ")
        print("\n")
        filename_2 = open(filename, "r")
        print(filename + ":")
        print(filename_2.read())
        print("\n")
        long_line()
        intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        long_line()
        intro()


def note_3():
    """ This function allows user to
        edit an existing file """
    try:
        filename = input("Which file do you want to edit?: ")
        print("\n")
        filename_2 = open(filename, "r")
        print(filename + ":")
        print(filename_2.read())
        print("\n")
        add_note = input("Do you want to add more? ")
        if add_note == "yes":
            add = input("What do you want to add:\n")
            with open(filename, "a+") as file_object:
                file_object.write("\n")
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write(add)
            print("\n")
            filename_3 = open(filename, "r")
            print(filename + ":")
            print(filename_3.read())
            print("\n")
            long_line()
            intro()
        if add_note == "no":
            long_line()
            intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        long_line()
        intro()


def note_4():
    """ This functions allows user to delete an existing file """
    try:
        filename = input("Which file do you want to delete?: ")
        print("\n")
        filename_2 = open(filename, "r")
        print(filename + ":")
        print(filename_2.read())
        print("\n")
        delete = input("Do you want to delete file: ")
        if delete == "yes":
            os.remove(filename)
            print("file : '" + filename + "'" + " is deleted")
            long_line()
            intro()
        if delete == "no":
            long_line()
            intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        long_line()
        intro()


while True:
    main_menu()
    intro()