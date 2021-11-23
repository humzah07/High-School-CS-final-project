# Course: CS 30
# Period: 2
# Date created: 23/11/21
# Date last modified: 22/11/21
# Name: Humzah Zahid Malik
# Description: Large Scale program

def main_menu():
    print(""" Hi!, Welcome to the Notes Program 
    
  In this program, you will be able to create, edit and delete notes.
  
  You will be allowed maximum 10 notes on this program. 
  
  *Notes*: Press space at the start when editing an existing file. 
           Press enter to start a new line""")
    print("\n")

valid_actions = ["a: create a file", "b: edit a file", "c: delete a file", "d: Close the program"]

def menu():
    print(""" Choose an action: """)
    for action in valid_actions:
        print(f" {action} ")

def intro():
  input("What would you like to do today? ")
  if input == "a":
    note_1()

def note_1():
  filename = input("What is the title of the note: ")
  character = input("What do you want to note today? ")
  with open(filename, 'w') as file_object:
    file_object.write(character)
  filename_2 = open(filename, "r")
  print(filename_2.read())


main_menu()
menu()
intro()
note_1()