ADMINPASSWORD = '0123456789'

while True:
    menuSelection = input('Select 1 for admin setup, 2 for login, or 3 to quit:')
    if menuSelection == '1':
        enteredPassword = input('Please enter the admin password:')
        if enteredPassword == ADMINPASSWORD:
            setupEntry = input('Welcome to admin setup. Please select 1 to add an account, select 2 to delete an account, select 3 to quit')
            ### Enter if loop for this menu
        elif enteredPassword == 'QUIT':
            break
        else:
            enteredPassword = input('Incorrect password, please enter the admin password or type QUIT to exit')
            continue
    elif menuSelection == '2':
        while True:
            ### Design to check values from a library
            print('Who are you?')
            name = input()
            if name == 'Lucas':
                password = input('Hello, Lucas. What is the password? (It is Gaelic.)')
                while password != 'Brogan':
                    print('Wrong password, please try again.')
                    password = input()
                while password == 'Brogan':
                    print('Access granted.')
                    break
                break
            elif name == 'Cody':
                password = input('Hello, Cody. What is the password? (You ringed, ranged, runged her finger.)')
                while password != 'Michala':
                    print('Wrong password, please try again.')
                    password = input()
                while password == 'Michala':
                    print('Access granted.')
                    break
                break
            else:
                name = input('Name not in system, please enter a satisfactory name or type QUIT to exit.')
                if name == 'QUIT':
                    break
                else:
                    continue
        break
    elif menuSelection == '3':
        print('System still armed, please restart to disarm system')
        break
    elif menuSelection == '2':
        while True:
            ### Design to check values from a library
            print('Who are you?')
            name = input()
            if name == 'Lucas':
                password = input('Hello, Lucas. What is the password? (It is Gaelic.)')
                while password != 'Brogan':
                    print('Wrong password, please try again.')
                    password = input()
                break
            elif name == 'Cody':
                print ('Hello, Cody. What is the password? (You liked her so you must have put a ring on her.)')
                password = input()
                if password == 'Michala':
                    break
            else:
                continue
        print('Access granted.')
        break
    elif menuSelection == '3':
        print('System still armed, please restart to disarm system')
        break
    else:
        input('Invalid input. Select 1 for admin setup, 2 for login, or 3 to quit:')
