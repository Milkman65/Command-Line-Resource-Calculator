import time
space = "    "
stoneTotal = 0
woodTotal = 0
thatchTotal = 0
def total():
    print("|" * 70)
    print("Total Resources")
    print("Stone: {}{}Wood: {}{}Thatch: {}".format(stoneTotal,space,woodTotal,space,thatchTotal))
    
def mainMenu():
    print("x" * 70)    
    print("Stone: 1{}Wood: 2".format(space))
    print("Exit: 0")
    total() #prints total amount of resources
    choice = input("Select a option: ")
    if choice.isdigit() == False:
        print("You must choose a number, Reloading")
        time.sleep(3)
        mainMenu()
    elif int(choice) > 2 or int(choice) < 0:
        print("Input not in valid range, Reloading")
        time.sleep(3)
        mainMenu()
    elif int(choice) == 0:
        print("Thanks for using me :)")
        time.sleep(3)
        exit()
    elif int(choice) == 1: #Stone
        stone()
    elif int(choice) == 2: #Wood
        wood()
    else:
        print("All 'if' options exhausted, Reloading")
        time.sleep(3)
        mainMenu()
        
        
def stone():
    global stoneTotal
    global woodTotal
    global thatchTotal    
    print("x" * 70)
    print("Foundation: 1{}Wall: 2{}Cieling: 3".format(space,space))
    print("back: 0")
    total() #prints total amount of resources
    choice = input("Select a option: ")
    if choice.isdigit() == False:
        print("You must choose a number, Reloading")
        time.sleep(3)
        stone()
    elif int(choice) > 3 or int(choice) < 0:
        print("Input not in valid range, Reloading")
        time.sleep(3)
        stone()
    elif int(choice) == 0: #back
        mainMenu()
    elif int(choice) == 1: #Stone Foundation
        amount = input("How many do you want?: ")
        amount = int(amount)
        stoneTotal += 80 * amount
        woodTotal += 40 * amount
        thatchTotal += 30 * amount
        stone()    
    else:
        print("All 'if' options exhausted, Reloading")
        time.sleep(3)
        stone()
    
def wood():
    global stoneTotal
    global woodTotal
    global thatchTotal
    print("This is wood")
    

    


mainMenu()
    
