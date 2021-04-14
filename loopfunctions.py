import random

database = {}


def init():

    
    isValidOptionSelected = False
    print("Welcome to bankPB")


    while isValidOptionSelected == False:
        
        
        haveAccount = int(input("Do you have an account with us: 1 (Yes) 2 (No) \n"))
    
    if(haveAccount == 1):
            isValidOptionSelected = True

            login()

    elif(haveAccount == 2):
            isValidOptionSelected = True

            register()
        

    else:
        print("Invalid option selected, please try again.")
        bankOperation()

def login():
    
    print("============ Login to your account ============")
    

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
         if(accountNumber == accountNumberFromUser):
             bankOperation(userDetails[3])
            
                    
    print("Invalid account of password")
    login()   


def register():
    print("============= Create an account ===============")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Enter a password \n")

    accountNumber = generateAccountNumber()
        
    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Account created successfully")
    print("============================")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("============================")

    login()
    
def bankOperation(user):    
    
 #   print("Welcome %s %s" %  (user[0], user[1] ) )
    
  #  selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

   # if(selectedOption == 1):
    #        depositOperation()

    #elif(selectedOption == 2):
     #       withdrawalOperation()

    #elif(selectedOption == 3):
 #           logout()

#    elif(selectedOption == 4):
 #           exit()
       # else:
#        print("invalid option selected")
 #       bankOperation(user)

#def withdrawalOperation():
 #   print("withdrawal")

#def depositOperation():
 #   print("Deposit operations")    

#def exit():
 #   print("Exit")

    def generateAccountNumber():
    

        return random.randrange (1111111111, 9999999999)

  #      def logout():
        #login()

    print(generateAccountNumber()) 

    
### BANKING OPERATION ####
    #init():