from tkinter import *
from tkinter import PhotoImage

MultiplayerCount = 1

def __main__():
    global MultiplayerCount
    window = Tk()
    window.title('TicTacToe - The Game')
    window.resizable(height= False, width= False)

    # Pages :
    main_menu = Frame(window)
    single_player  = Frame(window)
    multi_player = Frame(window)
    win_screen = Frame(window)

    # Page switcher
    def switch_page(frame):
        frame.tkraise()

    # Arranging all frames
    for frames in (main_menu,single_player,multi_player,win_screen):
        frames.grid(row=0, column=0, sticky='news')

    switch_page(main_menu)

    # Images
    main_menu_image = PhotoImage(file = 'main_menu_imgs/main_menu_image.png')
    single_player_button_img = PhotoImage(file = 'main_menu_imgs/singleplayer_button.png')
    multi_player_button_img = PhotoImage(file= 'main_menu_imgs/multiplayer_image.png' )
    exit_button_img = PhotoImage(file= 'main_menu_imgs/exit_image.png')
    singlePlayerImage = PhotoImage(file ='singlePlayerImages/single_player_background.png')
    backButtonImage = PhotoImage(file='singlePlayerImages/backButtonImage.png')
    tile_image = PhotoImage(file ='singlePlayerImages/x_x.png')
    x_image = PhotoImage(file ='singlePlayerImages/x_move.png')
    o_image = PhotoImage(file='singlePlayerImages/o_move.png')

    # Lables
    background_main_menu = Label(main_menu,image = main_menu_image, bd = 0, bg = 'black')
    single_player_button = Label(main_menu,image= single_player_button_img,bd = 0,bg = 'black')
    multi_player_button = Label(main_menu,image= multi_player_button_img,bd = 0,bg = 'black')
    exit_button = Label(main_menu,image= exit_button_img,bd = 0,bg = 'black')

    # Gridding
    background_main_menu.grid(row = 0,column = 0,columnspan =100,rowspan = 100)
    single_player_button.grid(row= 42,column = 53)
    multi_player_button.grid(row = 52,column = 53)
    exit_button.grid(row = 62,column = 53)

    # Button Functions :
    def pressed_on_exit(exit):
        window.destroy()


    def single_player_pressed(a):
        switch_page(single_player)

    def multi_player_pressed(a):
        switch_page(multi_player)

    def clearTiles():
        _tile1.config(image= tile_image)
        _tile2.config(image= tile_image)
        _tile3.config(image= tile_image)
        _tile4.config(image= tile_image)
        _tile5.config(image= tile_image)
        _tile6.config(image= tile_image)
        _tile7.config(image= tile_image)
        _tile8.config(image= tile_image)
        _tile9.config(image= tile_image)

    def playAgainPressed(e):
        switch_page(multi_player)
        clearTiles()

    def returnToMainMenu(a):
        switch_page(main_menu)
        clearTiles()

    # win-screens

    x_winscreenImage = PhotoImage(file = 'multi_player_image/playerXwinscreen.png')
    o_winscreenImage = PhotoImage(file = 'multi_player_image/playerOwinscreen.png')
    playAgainButtonImage = PhotoImage(file = 'multi_player_image/play again button.png')
    mainmenuButtonImage=  PhotoImage(file= 'multi_player_image/main_menu.png')

    backgroundWinscreenX = Label(win_screen,image = x_winscreenImage,bd= 0)
    playAgainButton = Label(win_screen, image = playAgainButtonImage,bd = 0)
    mainMenuButton = Label(win_screen, image = mainmenuButtonImage, bd = 0)

    backgroundWinscreenX.grid(rowspan= 100,columnspan = 100)
    playAgainButton.grid(row = 55,column= 50)
    mainMenuButton.grid(row = 60,column= 50)

    playAgainButton.bind("<Button-1>", playAgainPressed)
    mainMenuButton.bind("<Button-1>", returnToMainMenu)


    # ----------------------- SINGLE PLAYER -------------------------------
    background_slngle_playeru = Label(single_player,image = singlePlayerImage, bd = 0, bg = 'black')
    backButton = Label(single_player, image = backButtonImage,bd = 0,bg = 'black')

    def button_click(button):
        pass

    tile1 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile1))
    tile2 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile2))
    tile3 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile3))
    tile4 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile4))
    tile5 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile5))
    tile6 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile6))
    tile7 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile7))
    tile8 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile8))
    tile9 = Button(single_player, image= tile_image,bd= 1,command = lambda : button_click(tile9))

    # functions
    def backButtonPressed(back):
        switch_page(main_menu)
        tile1.config(image= tile_image)
        tile2.config(image= tile_image)
        tile3.config(image= tile_image)
        tile4.config(image= tile_image)
        tile5.config(image= tile_image)
        tile6.config(image= tile_image)
        tile7.config(image= tile_image)
        tile8.config(image= tile_image)
        tile9.config(image= tile_image)

    background_slngle_playeru.grid(rowspan=100,columnspan=100)
    backButton.grid(row = 0,column=0)
    backButton.bind('<Button-1>',backButtonPressed)

    tile1.grid(row=9, column=13, columnspan=20)
    tile2.grid(row=9, column=34, columnspan=25)
    tile3.grid(row=9, column=52, columnspan=35)
    tile4.grid(row=10, column=13, columnspan=20, rowspan=38)
    tile5.grid(row=10, column=34, columnspan=25, rowspan=38)
    tile6.grid(row=10, column=52, columnspan=35, rowspan=38)
    tile7.grid(row=44, column=13, columnspan=20, rowspan=42)
    tile8.grid(row=44, column=34, columnspan=25, rowspan=42)
    tile9.grid(row=44, column=52, columnspan=35, rowspan=42)

    # ----------------- MULTIPLAYER -----------------
    playerXTurn = PhotoImage(file ='multi_player_image/playerXTurn.png')
    playerOTurn = PhotoImage(file ='multi_player_image/playerOTurn.png')
    refreshIconMultiplayer = PhotoImage(file ='singlePlayerImages/refresh_icon.png')
    drawScrene = PhotoImage(file = 'multi_player_image/drawScreen.png')

    background_multiplayer = Label(multi_player, image=playerXTurn, bd=0, bg='black')
    backButton = Label(multi_player, image=backButtonImage, bd=0, bg='black')
    refreshbutton = Label(multi_player, image=refreshIconMultiplayer, bd=0, bg='black')

    # Functiosn
    def playerX_Wins():
        switch_page(win_screen)
        backgroundWinscreenX.config(image = x_winscreenImage)

    def playerO_Wins():
        switch_page(win_screen)
        backgroundWinscreenX.config(image = o_winscreenImage)

    def multiplayer_input(button):
        global MultiplayerCount
        if button['image'] == 'pyimage7':
            if MultiplayerCount % 2 == 0:
                button.config(image = o_image)
                MultiplayerCount += 1
                background_multiplayer.config(image = playerXTurn)
            else:
                button.config(image = x_image)
                MultiplayerCount += 1
                background_multiplayer.config(image = playerOTurn)
        else:
            return None


        x_placed,y_placed = 'pyimage8','pyimage9'

        # check weather X won!
        if _tile1['image'] == x_placed and _tile2['image'] == x_placed and _tile3['image'] == x_placed:
            playerX_Wins()
        elif _tile4['image'] == x_placed and _tile5['image'] == x_placed and _tile6['image'] == x_placed:
            playerX_Wins()
        elif _tile7['image'] == x_placed and _tile8['image'] == x_placed and _tile9['image'] == x_placed:
            playerX_Wins()
        elif _tile1['image'] == x_placed and _tile4['image'] == x_placed and _tile7['image'] == x_placed:
            playerX_Wins()
        elif _tile2['image'] == x_placed and _tile5['image'] == x_placed and _tile8['image'] == x_placed:
            playerX_Wins()
        elif _tile3['image'] == x_placed and _tile6['image'] == x_placed and _tile9['image'] == x_placed:
            playerX_Wins()
        elif _tile1['image'] == x_placed and _tile5['image'] == x_placed and _tile9['image'] == x_placed:
            playerX_Wins()
        elif _tile3['image'] == x_placed and _tile5['image'] == x_placed and _tile7['image'] == x_placed:
            playerX_Wins()

        # check weather O won!
        if  _tile1['image'] == y_placed and _tile2['image'] == y_placed and _tile3['image'] == y_placed:
            playerO_Wins()
        elif _tile4['image'] == y_placed and _tile5['image'] == y_placed and _tile6['image'] == y_placed:
            playerO_Wins()
        elif _tile7['image'] == y_placed and _tile8['image'] == y_placed and _tile9['image'] == y_placed:
            playerO_Wins()
        elif _tile1['image'] == y_placed and _tile4['image'] == y_placed and _tile7['image'] == y_placed:
            playerO_Wins()
        elif _tile2['image'] == y_placed and _tile5['image'] == y_placed and _tile8['image'] == y_placed:
            playerO_Wins()
        elif _tile3['image'] == y_placed and _tile6['image'] == y_placed and _tile9['image'] == y_placed:
            playerO_Wins()
        elif _tile1['image'] == y_placed and _tile5['image'] == y_placed and _tile9['image'] == y_placed:
            playerO_Wins()
        elif _tile3['image'] == y_placed and _tile5['image'] == y_placed and _tile7['image'] == y_placed:
            playerO_Wins()

        # check for draw!
        if _tile1['image'] != 'pyimage7' and _tile2['image'] != 'pyimage7' and _tile3['image'] != 'pyimage7':
            if _tile4['image'] != 'pyimage7' and _tile5['image'] != 'pyimage7' and _tile6['image'] != 'pyimage7':
                if _tile7['image'] != 'pyimage7' and _tile8['image'] != 'pyimage7' and _tile9['image'] != 'pyimage7':
                    backgroundWinscreenX.config(image = drawScrene)
                    switch_page(win_screen)

    def refreshMultiPlayer(a):
        _tile1.config(image=tile_image,bg = 'white')
        _tile2.config(image=tile_image,bg = 'white')
        _tile3.config(image=tile_image,bg = 'white')
        _tile4.config(image=tile_image,bg = 'white')
        _tile5.config(image=tile_image,bg = 'white')
        _tile6.config(image=tile_image,bg = 'white')
        _tile7.config(image=tile_image,bg = 'white')
        _tile8.config(image=tile_image,bg = 'white')
        _tile9.config(image=tile_image,bg = 'white')

    _tile1 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile1))
    _tile2 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile2))
    _tile3 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile3))
    _tile4 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile4))
    _tile5 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile5))
    _tile6 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile6))
    _tile7 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile7))
    _tile8 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile8))
    _tile9 = Button(multi_player, image=tile_image, bd=0, command=lambda: multiplayer_input(_tile9))

    background_multiplayer.grid(rowspan=100, columnspan=100)
    backButton.grid(row=0, column=0)
    refreshbutton.grid(row = 0,columnspan= 16)
    _tile1.grid(row=9, column=13, columnspan=20)
    _tile2.grid(row=9, column=34, columnspan=25)
    _tile3.grid(row=9, column=52, columnspan=35)
    _tile4.grid(row=10, column=13, columnspan=20, rowspan=38)
    _tile5.grid(row=10, column=34, columnspan=25, rowspan=38)
    _tile6.grid(row=10, column=52, columnspan=35, rowspan=38)
    _tile7.grid(row=44, column=13, columnspan=20, rowspan=42)
    _tile8.grid(row=44, column=34, columnspan=25, rowspan=42)
    _tile9.grid(row=44, column=52, columnspan=35, rowspan=42)

    exit_button.bind("<Button-1>", pressed_on_exit)
    single_player_button.bind("<Button-1>", single_player_pressed)
    multi_player_button.bind("<Button-1>", multi_player_pressed)
    backButton.bind('<Button-1>',backButtonPressed)
    refreshbutton.bind('<Button-1>',refreshMultiPlayer)

    window.geometry('722x600')
    window.mainloop()

if __name__ == '__main__':
    __main__()
