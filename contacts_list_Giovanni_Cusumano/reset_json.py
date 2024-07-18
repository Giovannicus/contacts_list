import json

def reset_json(contacts):
    
    '''
    Resets contacts.json in order to work with a default contacts list
    '''
    
    contacts = {}
    contacts['Rossi'] = {}
    contacts['Rossi']['Mario'] = {}
    contacts['Rossi']['Mario']['21/3/1990'] = "0123456789"

    contacts['Piccinini'] = {}
    contacts['Piccinini']['Enzo'] = {}
    contacts['Piccinini']['Enzo']['5/6/1951'] = "4725547454"

    contacts['Rossi']['Saverio'] = {}
    contacts['Rossi']['Saverio']['1/3/1980'] = "0455656669"

    contacts['Skel'] = {}
    contacts['Skel']['Jack'] = {}
    contacts['Skel']['Jack']['31/10/1993'] = "6732636167"

    with open("contacts.json","w+") as json_file:
        json.dump(contacts,json_file,indent=3)
    print("Contact list reset\n")
    return contacts;