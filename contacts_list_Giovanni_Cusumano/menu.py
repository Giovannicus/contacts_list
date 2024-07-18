import options as op
from reset_json import reset_json

def menu(option,contacts):
  while True:
    print("Enter the number corresponding to one of the following operations:")
    print("1: add, 2: modify, 3: delete, 4: search, 5: view contacts list, 6: reset, 7: exit\n")
    i = input();
    if i.isdigit():
        if int(i) in range(1,6):
            option[int(i)](contacts)
        elif int(i) == 6:
            print("This action is going to reset contact list, data will be set to default\n")
            contacts = reset_json(contacts) if input("Press 'y' to reset, any other to continue.\n").lower()=="y" else contacts
        elif int(i) == 7:
            op.exit_cl(contacts)
            break;
        else:
          print("Enter a valid number\n")
    else:
          print("Enter a valid number\n")