from defines import *
import addserver
import deleteserver
import main

if __name__ == '__main__':
    cprint('Welcome to the main menu', 'yellow')
    try:
        while True:
            cprint('1. Start the program', 'blue')
            cprint('2. Add a server', 'blue')
            cprint('3. Delete a server', 'blue')
            cprint('4. Exit', "red")
            select = input(colored('Please select: ', 'green'))
            if select == '1':
                main.main()
            elif select == '2':
                addserver.main()
            elif select == '3':
                deleteserver.main()
            elif select == '4':
                cprint('Bye', 'yellow')
                exit(0)
            else:
                print('Invalid')
    except KeyboardInterrupt:
        cprint('Bye', 'yellow')
        exit(0)