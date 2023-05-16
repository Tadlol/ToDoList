# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# TTharp, 05.11.2023, Wrote code for Step 1 & Step 3 & Step 6.
# TTharp, 05.12.2023, Wrote code for Step 4 & Step 6.
# TTharp, 05.13.2023, Revised Step 3 & Started code for Step 5.
# TTharp, 05.15.2023, Wrote code for Step 7 & Revised Step 5.
# TTharp, 05.15.2023, Code / comment cleanup, worked through project errors.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"
objFile = None  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows 
strChoice = ""  # A Capture the user option selection
strNewTask = ""  # Title of new task
strNewPri = ""  # Priority of new task
strRemTask = ""  # Task to remove
strExit = ""  # Exit choice
strSavExit = ""  # Save before exit choice

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(strFile, "r")
    for row in objFile:
        strData = row.split(",")
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
    print("ToDo List imported successfully!")
except:
    print("Starting a new Todo List!")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options:
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File.
    5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for dicRow in lstTable:
            print(dicRow["Task"] + "," + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strNewTask = input("Enter a new task: ")
        strNewPri = input("Enter " + strNewTask + "'s priority:")
        dicRow = {"Task": strNewTask, "Priority": strNewPri}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strRemTask = input("What task would you like to remove? ")
        for dicRow in lstTable:
            if dicRow["Task"].lower() == strRemTask.lower():
                lstTable.remove(dicRow)
                print(strRemTask + " has been removed from the ToDo List.")
                break
        else:
            print(strRemTask + " is not on the ToDo List1.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file - overwrites existing file at location.
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("Your ToDo List has been saved!")
        continue
    # Step 7 - Exit program with save check and confirmation
    elif strChoice.strip() == '5':
        strExit = input("Did you save your ToDo List already? (y/n)")
        if strExit.lower() == 'n':
            strSavExit = input("Do you want to save your ToDo List before exiting? (y/n)")
            if strSavExit.lower() == 'y':
                objFile = open(strFile, "w")
                for dicRow in lstTable:
                    objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
                objFile.close()
                print("Your ToDo List has been saved!")
                print("The program will now close.")
            elif strSavExit.lower() == 'n':
                print("The program will now close.")
            break
        elif strExit.lower() == 'y':
            print("The program will now close.")
        break  # and Exit the program
