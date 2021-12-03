# Course: CS 30
# Period: 2
# Date created: 23/11/21
# Date last modified: 01/12/21
# Name: Humzah Zahid Malik
# Description: Large Scale program


import os
import create_file
import view_files
import edit_files
import delete_files

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
        create_file.note_1()
    if input_1 == "b":
        view_files.note_2()
    if input_1 == "c":
        edit_files.note_3()
    if input_1 == "d":
        delete_files.note_4()
    if input_1 == "e":
        print(" You have closed the program ")
        quit()
    if input_1 not in valid_actions:
        print("invalid action")
        line()


def line():
    """ This creates a line between the output to seperate code """
    print("------------------------------------------------------------------")


while True:
    main_menu()
    intro()
