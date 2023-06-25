#A simple calculator app, "+ - */" with two numbers.
#If you what to enter from the calculation write stop.

#Create a variable for the user's filename. 

file_user = input("Enter file name:\nYou don't need to add the '.txt' at the end*\t")
file_user_calculation = (f"{file_user}.txt")
    #Take data from the user.
while True:
    while True:
        try:
            first_number = input("\nEnter the first number?\t")
            first_number = int(first_number)
            #Checking the entered value first number.
            break
        except ValueError:
            print("Please enter correct first number")

    operator = input("Enter operator? +  -  *  /\t") #User enter operator

    while True:
        try:
            second_number = input("Enter the second number?\t")
            second_number = int(second_number)
            break
        #Checking the entered value second number.
        except ValueError:
            print("Please enter correct second number")

    #Meetings calculator.
    if (operator == "/"): 
    #Checking divide by zero.
        try: 
            
            result = first_number / second_number
        
        except ZeroDivisionError: 
            result = "Oops, you can't divide by zero."
            print(result)
            
    
    elif (operator == "+"):
            result = first_number + second_number
            
            
    elif (operator == "-"):
            result = first_number - second_number
            
    elif (operator == "*"):
            result = first_number * second_number
            
        
                                          
                    
    #Checking if the operator is entered correctly.
    else:
        print("Please enter one of the suggested operations.")  
        operator = input("Please enter the operator correctly: +  -  *  /\t")
            
    
    #Show result.
    final_result = (f"\n{first_number} {operator} {second_number} = {result}")
    print(final_result) 
        
    # do stuff with file here  
    try:
        user_fail = open(file_user_calculation, 'a')
        user_fail.write(final_result)

    except FileNotFoundError as error:
            print("The file that you are trying to open does not exist")        
    
    finally:
        if user_fail is not None:
            user_fail.close()  

    # Menu
    print("1.If you want finish")
    print("2.If you want to read all of the equations")
    print("3.If you want to continue calculation ") #You can press any button.
    menu_choose = input("Select a menu item by entering a number (1-3)")
    
    #1.If you want finish STOP program
    if str(menu_choose) ==  "1":

    #2.If you want to read all of the equations  
        print("You are done with the calculator.")
    elif str(menu_choose) ==  "2":
        while True:
            file_user = input("Enter file name, which file you want to read from: \nYou don't need to add the '.txt' at the end*\t")
            try:
                user_fail = open(file_user_calculation, 'r')
                print(user_fail.read())
                user_fail.close() 
                break
            except ValueError:
                print("The filename is incorrect, please try again")   
                    