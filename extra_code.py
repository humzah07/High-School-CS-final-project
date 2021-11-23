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