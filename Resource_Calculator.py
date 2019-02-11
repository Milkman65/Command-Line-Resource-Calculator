import time

space = "    "
resource_dic = {"stone": 0, "wood": 0, "thatch": 0, "fungalwood": 0, "cp": 0, "fiber": 0}

def total(): #prints total amount of resources needed
    print("|" * 70)
    print("Total Resources")
    for i in resource_dic:
        if resource_dic[i] == 0:
            return
        else:
            #mess with formating 
            print(i, resource_dic[i])
    
def mainMenu():
    print("x" * 70)    
    print("Stone: 1{}Wood: 2".format(space))
    print("Exit: 0")
    total() #prints total amount of resources
    choice = quickIn("select")
    #error checking
    if choice.isdigit() == False:
        print("You must choose a number, Reloading")
        time.sleep(3)
        mainMenu()
    elif int(choice) > 2 or int(choice) < 0:
        print("Input not in valid range, Reloading")
        time.sleep(3)
        mainMenu()
    #menu system
    elif int(choice) == 0:
        print("Thanks for using me :)")
        time.sleep(3)
        exit()
    elif int(choice) == 1: #Stone
        stoneMenu()
    elif int(choice) == 2: #Wood
        wood()
    else:
        print("All 'if' options exhausted, Reloading")
        time.sleep(3)
        mainMenu()
               
def stoneMenu():
    global resource_dic   
    print("x" * 70)
    print("Foundation: 1{}Wall: 2{}Ceiling: 3".format(space,space))
    print("back: 0")
    total() #prints total amount of resources
    choice = quickIn("select")
    #error checking
    if choice.isdigit() == False:
        print("You must choose a number, Reloading")
        time.sleep(3)
        stoneMenu()
    elif int(choice) > 3 or int(choice) < 0:
        print("Input not in valid range, Reloading")
        time.sleep(3)
        stoneMenu()
    #menu system
    elif int(choice) == 0: #back
        mainMenu()
    elif int(choice) == 1: #Stone Foundation
        amount = int(quickIn(None))
        StoneStruct.stoneFoundation(amount)
        stoneMenu()
    elif int(choice) == 2: #Stone Wall
        amount = int(quickIn(None))
        StoneStruct.stoneWall(amount)
        stoneMenu()
    elif int(choice) == 3: #Stone Ceiling
        amount = int(quickIn(None))
        StoneStruct.stoneCeiling(amount)
        stoneMenu()  
    else:
        print("All 'if' options exhausted, Reloading")
        time.sleep(3)
        stoneMenu()

def quickIn(param): #makes coding in inputs less space consuming
    if param ==  "select":
        amount = input("Select a option: ")
        return amount
    else:
        amount = input("How many do you want?: ")
        return amount

def woodMenu():
    global resource_dic
    print("This is wood")
    
class StoneStruct(object): #Class that calculates all the values of stone structs
    def __init__(self, amount):
        self.amount = amount
        
    def stoneFoundation(amount):
        global resource_dic
        resource_dic["stone"] += 80 * amount
        resource_dic["wood"] += 40 * amount
        resource_dic["thatch"] += 30 * amount
        
    def stoneWall(amount):
        global resource_dic
        resource_dic["stone"] += 40 * amount
        resource_dic["wood"] += 20 * amount
        resource_dic["thatch"] += 15 * amount

    def stoneCeiling(amount):
        global resource_dic
        resource_dic["stone"] += 60 * amount
        resource_dic["wood"] += 30 * amount
        resource_dic["thatch"] += 20 * amount

    def stoneDoorframe(amount):
        global resource_dic
        resource_dic["stone"] += 30 * amount
        resource_dic["wood"] += 16 * amount
        resource_dic["thatch"] += 12 * amount

    def stoneDinogate(amount):
        global resource_dic
        resource_dic["stone"] += 280 * amount
        resource_dic["wood"] += 140 * amount
        resource_dic["thatch"] += 100 * amount

    def stoneCliffplatform(amount):
        global resource_dic
        resource_dic["stone"] += 1200 * amount
        resource_dic["wood"] += 800 * amount
        resource_dic["fiber"] += 600 * amount
        resource_dic["cp"] += 250 * amount

    def stoneStaircase(amount):
        global resource_dic
        resource_dic["stone"] += 200 * amount
        resource_dic["wood"] += 100 * amount
        resource_dic["thatch"] += 75 * amount
        
mainMenu()
    
