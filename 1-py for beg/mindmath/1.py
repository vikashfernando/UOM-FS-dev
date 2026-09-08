#data
validInputs=["1","2","3","4","5","6","#"]


#functions
#function1 - main menu
def mainMenu():   
    print("*"*40)
    print(" "*14+"xxxxx xxx")
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
    userInput=input("enter: ")
    inputValidation(userInput)

# function3 - validate inputs
def inputValidation(userInput):
    if userInput in validInputs:
        print("valid input")
        operations(userInput)
    else:
        print("invalid input")

# function4 - operations
def operations(userInput):
    if userInput=="1":
        print("add mode")
        number1=input("number 1: ")
        number2=input("number 2: ")
        add(number1,number2)
    elif userInput=="2":
        print("sub mode")
        number1=input("number 1: ")
        number2=input("number 2: ")
        sub(number1,number2)
    elif userInput=="3":
        print("mul mode")
        number1=input("number 1: ")
        number2=input("number 2: ")
        mul(number1,number2)
    elif userInput=="4":
        print("div mode")
        number1=input("number 1: ")
        number2=input("number 2: ")
        div(number1,number2)
    elif userInput=="5":
        print("pow mode")
        number1=input("number 1: ")
        number2=input("number 2: ")
        pow(number1,number2)
    elif userInput=="6":
        print("rem mode")
        number1=input("number 1: ")
        number2=input("number 2: ")
        rem(number1,number2)
    elif userInput=="$":
        print("$ detected")
    else:
        print("# detected")

# function5 - to get 2 inputs
def getOperationsInputs():
    number1=input("number 1: ")
    number2=input("number 2: ")






#--------------------------------------------

        
#function4 - "+"
def add(number1,number2):
    answer=int(number1)+int(number2)
    return answer

#function5 - "-"
def sub(number1,number2):
    answer=int(number1)-int(number2)
    return answer

#function6 - "*"
def mul(number1,number2):
    answer=int(number1)*int(number2)
    return answer

#function7 - "/"
def div(number1,number2):
    answer=int(number1)/int(number2)
    return answer

def pow(number1,number2):
    answer=int(number1)**int(number2)
    return answer

def rem(number1,number2):
    answer=int(number1)%int(number2)
    return answer


#--------------------------------------------








#function - calling program
def mainProgram():
    mainMenu()
    getInput()




#start
mainProgram()