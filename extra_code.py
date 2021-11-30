def first_note():
  filename = 'user.txt'
  character = input("What do you want to note today? ")
  with open(filename, 'w') as file_object:
    file_object.write(character)
  filename_2 = open("user.txt", "r")
  print(filename_2.read())
  
def first_note_add():
  filename = 'user.txt'
  add_note = input("Do you want to add more? ")
  if add_note == "yes":
    add = input("What do you want to add:\n")
    with open(filename, 'a') as file_object:
      file_object.write(add)
    filename_3 = open("user.txt", "r")
    print(filename_3.read())
  if add_note == "no":
    quit()  


file_object.seek(0)
data = file_object.read(100)
if len(data) > 0 :
file_object.write("\n")


valid_actions = ["a: create a file", "b: view a file", "c: edit a file", "d: delete a file", "e: Close the program"]

def menu():
    print(""" Choose an action: """)
    for action in valid_actions:
        print(f" {action} ")

valid_actions_1 = ["a", "b", "c", "d", "e"]