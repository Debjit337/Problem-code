''' 
Sir code toh erroe nehi hai par string value dene ke baad message se bahar nikal deh raha hai.
Bas yehi problem hai matlab uske baad message phir se call nehi ho raha hai.kya karu?
'''
# again choice
def again_choice():
    # user se option ke liye condtion
    message = '''
    ---------------------------------
        Welcome to Calculator
    ---------------------------------
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Exit
    ---------------------------------
    Note: Remeber only enter numbers.(Exit:4)
    Enter 1 or 2 or 3 for any of calulation:    
    '''
      
    # check choice if 1 then show hello
    if option == 1:
        # print('\nHello')
        addition()
    # check choice if 2 then show hi
    elif option == 2:
        #print('\nHi')
        subtraction()
    # check if choice is wrong then show wrong
    elif option == 3:
        #print('\n3')
        multiplication()
    elif option == 4:
        print('\nExit')
    else:
       print('\nYou enter wrong choice. Try again')

# addition function
def addition():
    try:
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
    except:  
        print('\nOnly allow integer numbers.')
        again_choice()
    else:      
        sum = a + b
        print('\nAddition answer: ', sum)
        # dubara choice show karane ke liye again choice function banaya hai.
        again_choice()

# subtraction function
def subtraction():
    try:
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
    except:
        print('\nOnly allow integer numbers.')
        again_choice()
    else:       
        sum = a - b
        print('\nSubtraction answer: ', sum)
        again_choice()

# multiplication function
def multiplication():
    try:
        a = int(input('Enter 1st number: '))
        b = int(input('Enter 2nd number: '))
    except:
        print('\nOnly allow integer numbers.')
        again_choice()
    else:    
        sum = a * b
        print('\nMultiplication answer: ', sum)
        again_choice()



# user se option ke liye condtion
message = '''
---------------------------------
    Welcome to Calculator
---------------------------------
1. Addition
2. Subtraction
3. Multiplication
4. Exit
---------------------------------
Note: Remeber only enter numbers.(Exit:4)
Enter 1 or 2 or 3 for any of calulation:    
'''
try:
        option = int(input(message))
except:
        print('\nOnly integer number.') 
else:       
    # check choice if 1 then show hello
    if option == 1:
        # print('\nHello')
        addition()
    # check choice if 2 then show hi
    elif option == 2:
        #print('\nHi')
        subtraction()
    # check if choice is wrong then show wrong
    elif option == 3:
        #print('\n3')
        multiplication()
    elif option == 4:
        print('\nExit')
    else:
       print('\nYou enter wrong choice. Try again')
       
    
