#data
validInputs=["1","2","3","4","5","6","#","$"]


#functions
#function1 - main menu
def mainMenu():   
    print("*"*40)
    print(" "*14+"Smart Cal")
    print("*"*40)
    print(" ")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. **")
    print("6. %")
    print(" ")
    print("> enter '#' to terminate the program")
    print("> enter '$' to reset")
    print(" ")
    print("*"*40)


# function2 - get inputs from user
def getInput():
    userInput=input("input: ")
    while inputValidation(userInput)!=1:
        mainMenu()
        getInput()

#function3 - validate inputs
def inputValidation(num):
    if num in validInputs:
        return 1
        
#function4 - "+"
def add(number1,number2):
    ans+



#function - calling program
def mainProgram():
    mainMenu()
    getInput()




#start
mainProgram()