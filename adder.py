import json
import display
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(script_dir, "time.json")
def checkIfExist(data,name):
    if name in data:
        return True
    return False

def create(data,name):
    data[name] = [0,""]

def quit(name):
    if name == "q":
        return True
    return False

def run():
    with open(FILE,"r") as f:
        data = json.load(f)
    name = input("Please give the name or quit.\n")
    check = checkIfExist(data,name)
    if quit(name):
        print("Exiting")
        return
    while check:
        print()
        print("This is already tracked. See list of tracked objects below")
        display.run()
        name = input("Please choose a new name or quit.\n")
        if quit(name):
            print("Exiting")
            return
        check = checkIfExist(data,name)
    print()

    create(data,name)

    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)

### NOT INTERACTIVE
def runCLI(args):
    try:
        name = args[0]
        with open(FILE,"r") as f:
            data = json.load(f)
        check = checkIfExist(data,name)
        if check:
            print("This object already exists.")
            return
        create(data,name)
        print("Object created")
        with open(FILE,"w") as f:
            json.dump(data,f,indent=4)
    except:
        print("ERROR. Incompatible amount of args")
        return
