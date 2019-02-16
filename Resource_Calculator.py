import time

space = "    "
resource_dic = {"Stone": 0, "Wood": 0, "Thatch": 0, "Fungal Wood": 0, "CP": 0, "Fiber": 0}
item_dic = {
#Thatch 
"Sloped Thatch Roofs": 0, #add
"Sloped Thatch Walls Right": 0, #add
"Sloped Thatch Walls Left": 0, #add
"Thatch Doors": 0, #add
"Thatch Roofs": 0, #add
"Thatch Door Frames": 0, #add
"Thatch Walls": 0, #add
"Thatch Foundations": 0, #add
#Wood
"Wood Staircases": 0, #add
"Wood Railings": 0, #add
"Wood Fence Foundations": 0, #add
"Wood Ramps": 0, #add
"Sloped Wood Roofs": 0, #add
"Sloped Wood Walls Left": 0, #add
"Sloped Wood Walls Right": 0, #add
"Dinosaur Gates": 0, #add
"Dinosaur Gateways": 0, #add
"Wood Catwalks": 0, #add
"Wood Pillars": 0, #add
"Wood Ladders": 0, #add
"Wood Trapdoors": 0, #add
"Wood Hatch Frames": 0, #add
"Wood Windows": 0, #add
"Wood Window Frames": 0, #add
"Wood Doors": 0, #add
"Wood Ceilings": 0, #add
"Wood Door Frames": 0, #add
"Wood Walls": 0, #add
"Wood Foundations": 0, #add 
#Stone 
"Stone Staircases": 0, #add
"Stone Railings": 0, #add
"Stone Fence Foundations": 0, #add
"Behemoth Reinforced Dinosaur Gates": 0, #add
"Behemoth Stone Dinosaur Gateways": 0, #add
"Sloped Stone Roofs": 0, #add
"Sloped Stone Walls Left": 0, #add
"Sloped Stone Walls Right": 0, #add
"Reinforced Dinosaur Gates": 0, #add
"Stone Dinosaur Gateways": 0, 
"Stone Pillars": 0, #add
"Reinforced Trapdoors": 0, #add
"Stone Hatch Frames": 0, #add
"Stone Window Frames": 0, #add
"Reinforced Windows": 0, #add
"Reinforced Wooden Doors": 0, #add
"Stone Ceilings": 0,
"Stone Door Frames": 0,
"Stone Walls": 0,
"Stone Foundations": 0,
#Green House 
"Sloped Greenhouse Walls Right": 0, #add
"Sloped Greenhouse Walls Left": 0, #add
"Sloped Greenhouse Roofs": 0, #add
"Greenhouse Windows": 0, #add
"Greenhouse Doors": 0, #add
"Greenhouse Ceilings": 0, #add
"Greenhouse Door Frames": 0, #add
"Greenhouse Walls": 0, #add
#Metal 
"Metal Staircases": 0, #add
"Metal Railings": 0, #add
"Metal Fence Foundations": 0, #add
"Behemoth Gates": 0, #add
"Behemoth Gateways": 0, #add
"Metal Ramps": 0, #add
"Sloped Metal Roofs": 0, #add
"Sloped Metal Walls Left": 0, #add
"Sloped Metal Walls Right": 0, #add
"Metal Dinosaur Gates": 0, #add
"Metal Dinosaur Gateways": 0, #add
"Metal Catwalks": 0, #add
"Metal Pillars": 0, #add
"Metal Ladders": 0, #add
"Metal Trapdoors": 0, #add
"Metal Hatch Frames": 0, #add
"Metal Window Frames": 0, #add
"Metal Windows": 0, #add
"Metal Doors": 0, #add
"Metal Ceilings": 0, #add
"Metal Door Frames": 0, #add
"Metal Walls": 0, #add
"Metal Foundations": 0, #add
#Tek 
"Vacuum Compartment Moonpool": 0, #add
"Vacuum Compartment": 0, #add
"Tek Staircases": 0, #add
"Tek Railings": 0, #add
"Tek Fence Foundations": 0, #add
"Behemoth Tek Gates": 0, #add
"Behemoth Tek Gateways": 0, #add
"Tek Ramps": 0, #add
"Sloped Tek Roofs": 0, #add
"Sloped Tek Walls Left": 0, #add
"Sloped Tek Walls Right": 0, #add
"Tek Dinosaur Gates": 0, #add
"Tek Dinosaur Gateways": 0, #add
"Tek Catwalks": 0, #add
"Tek Pillars": 0, #add
"Tek Ladders": 0, #add
"Tek Trapdoors": 0, #add
"Tek Hatch Frames": 0, #add
"Tek Window Frames": 0, #add
"Tek Windows": 0, #add
"Tek Doors": 0, #add
"Tek Ceilings": 0, #add
"Tek Door Frames": 0, #add
"Tek Walls": 0, #add
"Tek Foundations": 0, #add
#Storage 
"Storage Boxes": 0, #add
"Large Storage Boxes": 0, #add
"Water Tanks": 0, #add
"Metal Water Reservoirs": 0, #add
"Feeding Trough": 0, #add
"Bookshelfs": 0, #add
"Vaults": 0, #add
"Preserving Bins": 0, #add
"Refrigerators": 0, #add
"Vessels": 0, #add
"Gas Collectors": 0, #add
#Crafting 
"Campfires": 0, #add
"Mortar And Pestles": 0, #add
"Cooking Pots": 0, #add
"Refining Forges": 0, #add
"Smithys": 0, #add
"Beer Barrels": 0, #add
"Fabricators": 0, #add
"Industrial Grills": 0, #add
"Industrial Grinders": 0, #add
"Industrial Forges": 0, #add
"Chemistry Benchs": 0, #add
"Industrial Cookers": 0, #add
"Tek Replicators": 0, #add
#Farming 
"Small Crop Plots": 0, #add
"Medium Crop Plots": 0, #add
"Large Crop Plots": 0, #add
"Compost Bins": 0, #add
"Stone Irrigation Pipes - Inclined": 0, #add
"Stone Irrigation Pipes - Intersection": 0, #add
"Stone Irrigation Pipes - Straight": 0, #add
"Stone Irrigation Pipes - Tap": 0, #add
"Stone Irrigation Pipes - Vertical": 0 #add
}

#Fill out Classes with accurate resource costs for all of the above dictionary entries.

def help():
    print("Hello this is an application made by Milkman65. If you would like to contribute any ideas or code to this project please check out my github(https://github.com/Milkman65).")
    print(" ")
    print("Basic use of this application requires the user to type the assigned value(right) of a topic(left) as seen on the UI.")
    print("As an example to access the Stone Structure Menu if the UI looks like this 'Stone: 1' you would need to enter the input '1'.")
    print(" ")
    input("To get back to the main menu type anything and press enter: ")
    mainMenu()

def quickIn(param): #makes coding in inputs less space consuming
    if param ==  "select":
        amount = input("Select a option: ")
        return amount
    else:
        amount = input("How many do you want?: ")
        return amount

def totalResources(): #prints total amount of resources needed
    print("|" * 70)
    print("Total Resources and Items")
    print(" ")
    for i in resource_dic: #prints a key and its value if it isn't equal to 0
        if resource_dic[i] <= 0:
            continue
        else:
            print(i, resource_dic[i])

def totalStructures():
    print("Here is a list of the total amount of structures you've calculated")
    print()
    for i in item_dic: #prints a key and its value if it isn't equal to 0
        if item_dic[i] <= 0:
            continue    
        else:
            print(i, item_dic[i])
    print()
    input("Enter anything to continue: ")
    



def mainMenu():
    print("x" * 70)
    print("{}MAIN MENU{}".format(space * 4, space * 4)) 
    print()   
    print("Thatch: 1{}Wood: 2{}Stone: 3{}Greenhouse: 4".format(space,space,space))
    print()
    print("Metal: 5{}Tek: 6{}Storage: 7{}Crafting: 8".format(space,space,space))
    print()
    print("Farming: 9")
    print()
    print("Exit: 0{} Calculated: info{} Help: help".format(space,space))
    print()
    totalResources() #prints total amount of resources
    choice = quickIn("select")
    #error checking
    if choice.upper() == "INFO":
        totalStructures()
        mainMenu()
    elif choice.upper() == "HELP":
        help()
    elif choice.isdigit() == False:
        print("You must choose a number, Reloading")
        time.sleep(3)
        mainMenu()
    elif int(choice) > 9 or int(choice) < 0:
        print("Input not in valid range, Reloading")
        time.sleep(3)
        mainMenu()
    #menu system
    elif int(choice) == 0:
        print("Thanks for using me :)")
        time.sleep(3)
        exit()
    elif int(choice) == 1: #Thatch
        thatchMenu()
    elif int(choice) == 2: #Wood
        woodMenu()
    elif int(choice) == 3: #Stone
        stoneMenu()
    elif int(choice) == 4: #Greenhouse
        greenhouseMenu()
    elif int(choice) == 5: #Metal
        metalMenu()
    elif int(choice) == 6: #Tek
        tekMenu()
    elif int(choice) == 7: #Storage
        storageMenu()
    elif int(choice) == 8: #Crafting
        craftingMenu()
    elif int(choice) == 9: #Farming
        farmingMenu()
    else:
        print("All 'if' options exhausted, Reloading")
        time.sleep(3)
        mainMenu()

def thatchMenu():
    global resource_dic
    print("This is thatch")

def woodMenu():
    global resource_dic
    print("This is wood")
               
def stoneMenu():
    global resource_dic   
    print("x" * 70)
    print("{}STONE{}".format(space * 4, space * 4))
    print()
    print("Foundation: 1{}Wall: 2{}Ceiling: 3{}Door Frame: 4".format(space,space,space))
    print()
    print("Dino Gateway: 5{}Reinforced Door: 6".format(space))
    print()
    print("Back: 0{}Calculated: info".format(space))
    print()
    totalResources() #prints total amount of resources
    choice = quickIn("select")
    #error checking
    if choice.upper() == "INFO":
        totalStructures()
        stoneMenu()
    elif choice.isdigit() == False:
        print("You must choose a valid option, Reloading")
        time.sleep(3)
        stoneMenu()
    elif int(choice) > 6 or int(choice) < 0:
        print("Input is not recognized, Reloading")
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
    elif int(choice) == 4: #Stone Door Frame
        amount = int(quickIn(None))
        StoneStruct.stoneDoorframe(amount)
        stoneMenu()
    elif int(choice) == 5: #DinoGateway
        amount = int(quickIn(None))
        StoneStruct.stoneDinogateway(amount)
        stoneMenu()
    elif int(choice) == 6: #ReinforcedDoor
        amount = int(quickIn(None))  
    else:
        print("All 'if' options exhausted, Reloading")
        time.sleep(3)
        stoneMenu()

def greenhouseMenu():
    global resource_dic
    print("This is greenhouse")

def tekMenu():
    global resource_dic
    print("This is tek")

def storageMenu():
    global resource_dic
    print("This is storage")

def craftingMenu():
    global resource_dic
    print("This is crafting")

def farmingMenu():
    global resource_dic
    print("This is farming")
    



class ThatchStruct(object): #Class that calculates all the values of thatch structs
    def __init__(self, amount):
        self.amount = amount

class WoodStruct(object): #Class that calculates all the values of wood structs
    def __init__(self, amount):
        self.amount = amount

class StoneStruct(object): #Class that calculates all the values of stone structs
    def __init__(self, amount):
        self.amount = amount
        
    def stoneFoundation(amount):
        global resource_dic
        resource_dic["Stone"] += 80 * amount
        resource_dic["Wood"] += 40 * amount
        resource_dic["Thatch"] += 30 * amount
        item_dic["Stone Foundations"] += 1 * amount
        
    def stoneWall(amount):
        global resource_dic
        resource_dic["Stone"] += 40 * amount
        resource_dic["Wood"] += 20 * amount
        resource_dic["Thatch"] += 15 * amount
        item_dic["Stone Walls"] += 1 * amount

    def stoneCeiling(amount):
        global resource_dic
        resource_dic["Stone"] += 60 * amount
        resource_dic["Wood"] += 30 * amount
        resource_dic["Thatch"] += 20 * amount
        item_dic["Stone Ceilings"] += 1 * amount

    def stoneDoorframe(amount):
        global resource_dic
        resource_dic["Stone"] += 30 * amount
        resource_dic["Wood"] += 16 * amount
        resource_dic["Thatch"] += 12 * amount
        item_dic["Stone Door Frames"] += 1 * amount

    def stoneDinogateway(amount):
        global resource_dic
        resource_dic["Stone"] += 280 * amount
        resource_dic["Wood"] += 140 * amount
        resource_dic["Thatch"] += 100 * amount

    def stoneStaircase(amount):
        global resource_dic
        resource_dic["Stone"] += 200 * amount
        resource_dic["Wood"] += 100 * amount
        resource_dic["Thatch"] += 75 * amount
        
class GreenhouseStruct(object): #Class that calculates all the values of greenhouse structs
    def __init__(self, amount):
        self.amount = amount

class MetalStruct(object): #Class that calculates all the values of metal structs
    def __init__(self, amount):
        self.amount = amount

class TekStruct(object): #Class that calculates all the values of tek structs
    def __init__(self, amount):
        self.amount = amount

class StorageStruct(object): #Class that calculates all the values of storage structs
    def __init__(self, amount):
        self.amount = amount

class CraftingStruct(object): #Class that calculates all the values of crafting structs
    def __init__(self, amount):
        self.amount = amount

class FarmingStruct(object): #Class that calculates all the values of farming structs
    def __init__(self, amount):
        self.amount = amount




mainMenu()