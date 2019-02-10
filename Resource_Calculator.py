import time

def mainMenu():
    print("|" * 70)
    print("Stone: 1" + "    " + "Wood: 2")
    choice = input("Select a option: ")
    if choice.isdigit() == False:
        print("You must choose a number, exiting program")
        time.sleep(3)
        exit()
    elif int(choice) > 2 or int(choice) < 1:
        print("Input not in valid range, exiting program")
        time.sleep(3)
        exit()
    elif int(choice) == 1:
        stone()
    elif int(choice) == 2:
        wood()
    else:
        print("All if option exhausted, exiting program")
        time.sleep(3)
        exit()
        
        
def stone():
    print("This is stone")
def wood():
    print("This is wood")
    

mainMenu()
    
