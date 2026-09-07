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
    while True:
        userInput=input("input: ")

        if inputValidation(userInput)==True:
            print("test1-pass input validation")
            return userInput

            if userInput=="+":

                add(num1,num2)

#function3 - validate inputs
def inputValidation(num):
    return num in validInputs











#--------------------------------------------

        
#function4 - "+"
def add(number1,number2):
    answer=number1+number2
    return answer

#function5 - "-"
def sub(number1,number2):
    answer=number1-number2
    return answer

#function6 - "*"
def mul(number1,number2):
    answer=number1*number2
    return answer

#function7 - "/"
def div(number1,number2):
    answer=number1/number2
    return answer

#--------------------------------------------








#function - calling program
def mainProgram():
    mainMenu()
    getInput()




#start
mainProgram()