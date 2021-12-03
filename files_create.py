import main

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
    main.line()
    main.intro()