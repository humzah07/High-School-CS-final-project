import main

def note_2():
    """ This functions opens files in view mode """
    try:
        filename = input("Which file do you want to open?: ")
        print("\n")
        filename_2 = open(filename, "r")
        print(filename + ":")
        print(filename_2.read())
        print("\n")
        main.line()
        main.intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        main.line()
        main.intro()