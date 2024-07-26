from  import Game
def showMenu():
    selection = ''
    while selection != 'q':
        print ('menu placeholder press q and hit enter to continue')
        if selection == 1:
            enterGame()
        selection = input()