# Course: CS 30
# Period: 2
# Date created: 23/11/21
# Date last modified: 01/12/21
# Name: Humzah Zahid Malik
# Description: Large Scale program


import os

# Creates a menu of valid actions in this program


valid_actions = ["a: create a file", "b: view a file", "c: edit a file",
                 """d: delete a file""", """e: Close the program"""]


def main_menu():
    """ Prints the introduction of the program """
    print(""" Hi!, Welcome to the Notes Program

  In this program, you will be able to create,view, edit and delete notes.

  You can make unlimited files on this program

  *Notes*: Create a file first in order to access other features
           such as editing or viewing a File

           You can only write one line when creating a File.
           To add more, go to "edit a file" to add one line at a time.

           You can not have two files with the same name.
           New file created with the same name will overwrite the existing
           file's contents.

           When entering a file name, the name should be matching the 
           letter case of the file. 

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
    if input_1 not in valid_actions:
        print("invalid action")
        line()


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
    line()
    intro()

def line():
    """ This creates a line between the output to seperate code """
    print("------------------------------------------------------------------")


def note_2():
    """ This functions opens files in view mode """
    try:
        filename = input("Which file do you want to open?: ")
        print("\n")
        filename_2 = open(filename, "r")
        print(filename + ":")
        print(filename_2.read())
        print("\n")
        line()
        intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        line()
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
            line()
            intro()
        if add_note == "no":
            line()
            intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        line()
        intro()

def note_4():
    filename = input("Which file do you want to delete a line from: ")
    print("\n")
    filename_2 = open(filename, "r")
    print(filename + ":")
    print(filename_2.read())
    print("\n")
    delete_line = input("What line do you want to delete: ")
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        print(line.replace(delete_line, "hello"))


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
            line()
            intro()
        if delete == "no":
            line()
            intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        line()
        intro()


while True:
    main_menu()
    intro()
