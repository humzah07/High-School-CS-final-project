import main


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
            main.line()
            main.intro()
        if add_note == "no":
            main.line()
            main.intro()
    except FileNotFoundError:
        print("File does not exists. returning to main menu")
        main.line()
        main.intro()
