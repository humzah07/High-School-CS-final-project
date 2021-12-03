import os
import main

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
            main.line()
            main.intro()
        if delete == "no":
            main.line()
            main.intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        main.line()
        main.intro()