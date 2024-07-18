import json
import sys
from reset_json import reset_json
from initialization import initialization
from menu import menu
import options as op

if __name__ == "__main__":
    [option,contacts] = initialization()
    menu(option,contacts)
    sys.exit(0)