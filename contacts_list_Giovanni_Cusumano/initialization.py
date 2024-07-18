import json 
import options as op

def initialization():

    with open("contacts.json") as json_file:
        contacts = json.load(json_file)

    option = {
        1: op.add,
        2: op.modify,
        3: op.delete,
        4: op.search,
        5: op.contact_list,
    }
    return option,contacts    