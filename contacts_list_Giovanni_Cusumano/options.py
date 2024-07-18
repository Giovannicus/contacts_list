import json
from datetime import datetime
from menu import menu

def add(contacts):
    '''
        Adds a contact to contact list by manual input
    '''
    # get surname as input
    print("Insert record data\n")
    print("Surname\n")
    surn = input();
    if surn not in list(contacts.keys()):
        contacts[surn] = {};
    # get name as input
    print("Name\n")
    name = input();
    # get and validate birthdate as input til having a good one
    print("Birthdate(g/m/Y)\n")
    birth = input();
    while not _is_valid_date(birth):
        print("Invalid birthdate, try again\n")
        print("Birthdate(g/m/Y)\n")
        birth = input();
    # get and validate phone number as input til having a good one
    print("Phone number (10 digits)\n")
    phone = input();
    while not (len(phone)==10 and phone.isdigit()):
        print("Invalid phone number, try again\n")
        print("Phone number (10 digits)\n")
        phone = input();
    
    # evaluates to set a new contact or to add info to an exiting one
    if name not in contacts[surn]:
        contacts[surn][name] = {};
        contacts[surn][name][birth] = phone;
    else:
        if birth not in contacts[surn][name]:
            contacts[surn][name][birth] = phone;
        else:
            contacts[surn][name][birth]+= ', ' + phone;
    
    print(f"{surn} {name} Record added")
    _update(contacts);
    return contacts
    
def modify(contacts):

    '''
        Edit a chosen contact by manual input
    '''
    
    print("Type the surname you want to modify\n")
    surn = input();
    surn = _find(contacts,surn)
    # evaluates the given surname exists
    if isinstance(surn, str):
        if len(contacts[surn]) == 1:
            del contacts[surn];
            print(f"{surn} is going to be modified\n")
            return add(contacts)
        elif len(contacts[surn]) > 1:
            # allows choosing in case of  multiple contacts
            print("Which one?\n")
            for name in contacts[surn]:
                print(name)
            name = input();
            if name in contacts[surn]:
                del contacts[surn][name];
                print(f"{surn} {name} is going to be modified\n")
                return add(contacts)
            else:
                print(f"No {surn} {name} found, reset.\n")
                
    
def delete(contacts):
    '''
        Delete a chosen contact by manual input
    '''
    print("Type the surname you want to delete\n")
    surn = input();
    surn = _find(contacts,surn)
    if isinstance(surn, str):
        if len(contacts[surn]) == 1:
            print(f"{surn} Record deleted\n")
            del contacts[surn];
        elif len(contacts[surn]) > 1:
            print("Which one?\n")
            for name in contacts[surn]:
                print(name)
            name = input();
            if name in contacts[surn]:
                del contacts[surn][name];
                print(f"{surn} {name} Record deleted\n")
            else:
                print(f"No {surn} {name} found, reset.\n")

    _update(contacts)

def search(contacts):
    '''
        Search a chosen contact by manual input
    '''
    print("Insert surname\n")
    surn = input();
    surn = _find(contacts,surn)
    if isinstance(surn, str):
        print("Surname    Name       Birth      Phone\n")
        for name in contacts[surn]:
            for birth in contacts[surn][name]:
                print(f"{surn:<10} {name:<10} {birth:<10} {contacts[surn][name][birth]:<20}")


def contact_list(contacts):
    '''
        Displays full contacts list
    '''
    print("Surname    Name       Birth      Phone\n")
    for surn in contacts:
        for name in contacts[surn]:
            for birth in contacts[surn][name]:
                print(f"{surn:<10} {name:<10} {birth:<10} {contacts[surn][name][birth]:<20}")
                    
def exit_cl(contacts):
    _update(contacts)
    print("Exiting\n")

def _update(contacts):
    with open("contacts.json","w+") as json_file:
        json.dump(contacts,json_file,indent=3)
    print("Saved contacts list on json\n")
    
def _find(contacts,data):
    keys_list = list(contacts.keys());
    try: 
        surn = keys_list[keys_list.index(data)];
        return surn
    except:
        print(f"No {data} found, reset.\n")
        return 0

def _is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except:
        return False

    