while True:
    print('Who are you?')
    name = input()
    if name == 'Lucas':
        print ('Hello, Lucas. What is the password? (It is Gaelic.)')
        password = input()
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