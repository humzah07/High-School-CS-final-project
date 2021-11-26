# Course: CS 30
# Period: 2
# Date created: 23/11/21
# Date last modified: 22/11/21
# Name: Humzah Zahid Malik
# Description: Large Scale program

import os

def main_menu():
    print(""" Hi!, Welcome to the Notes Program 
    
  In this program, you will be able to create, edit and delete notes.
  
  You can make unlimited files on this program
  
  *Notes*: Create a file first in order to access other features such as 
   """)
    print("\n")

valid_actions = ["a: create a file", "b: view a file", "c: edit a file", "d: delete a file", "e: Close the program"]

def menu():
    print(""" Choose an action: """)
    for action in valid_actions:
        print(f" {action} ")

def intro():
  input_1 = input("What would you like to do today? ")
  if input_1 == "a":
    note_1()
  if input_1 == "b":
    note_2()
  if input_1 == "c":
    note_3()
  if input_1 == "d":
    note_4()


def note_1():
  filename = input("What is the title of the note: ")
  file_name = filename
  character = input("What do you want to note(Note down here below)? ")
  print("\n")
  with open(file_name, 'w') as file_object:
    file_object.write(character)
  filename_2 = open(filename, "r")
  print(filename_2.read())

def note_2():
  filename = input("Which file do you want to open?: ")
  print("\n")
  filename_2 = open(filename, "r") 
  print(filename_2.read())
  quit()

def note_3():
    filename = input("Which file do you want to open?: ")
    print("\n")
    filename_2 = open(filename, "r") 
    print(filename_2.read())
    add_note = input("Do you want to add more? ")
    if add_note == "yes":
        add = input("What do you want to add:\n")
        with open(filename, "a+") as file_object:
          file_object.write("\n")
          data = file_object.read(100)
          if len(data) > 0 :
              file_object.write("\n")
        file_object.write(add)
    if add_note == "no":
        quit() 

def note_4():
    filename = input("Which file do you want to open?: ")
    print("\n")
    filename_2 = open(filename, "r") 
    print(filename_2.read())
    print("\n")
    delete = input("Do you want to delete file: ")
    if delete == "yes":
      os.remove(filename)
    if delete == "no":
      main_menu()


while True:
  main_menu()
  menu()
  intro()
