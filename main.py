import random
from tkinter import *
from tkinter import PhotoImage

x_placed, y_placed = 'pyimage8', 'pyimage9'

MultiplayerCount = 1
tiles = ['tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7', 'tile8', 'tile9']
usedTiles = []

def __main__():
    global MultiplayerCount,x_placed,y_placed
    window = Tk()
    window.title('TicTacToe - The Game')
    window.resizable(height= True, width= True)

    # Pages :
    main_menu = Frame(window)
    single_player  = Frame(window)
    multi_player = Frame(window)
    win_screen = Frame(window)
    win_screenSingleplayer = Frame(window)

    # Page switcher
    def switch_page(frame):
        frame.tkraise()

    # Arranging all frames
    for frames in (main_menu,single_player,multi_player,win_screen,win_screenSingleplayer):
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
    AI_wins = PhotoImage(file = 'singlePlayerImages/AIwins.png')
    you_win = PhotoImage(file = 'singlePlayerImages/youwon.png')
    retry_button_image =  PhotoImage(file = 'multi_player_image/play again button.png')

    win_screenbackground = Label(win_screenSingleplayer,bd= 0,bg = 'black')
    win_screenbackground.grid(row = 0,column = 0)

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
    refresingleplayer = PhotoImage(file ='singlePlayerImages/refresh_icon.png')
    drawImage = PhotoImage(file = 'singlePlayerImages/draw_page.png')

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

    backgroundImageWinscreenSingle = Label(win_screenSingleplayer, image=AI_wins, bd=0)
    retry_button = Button(win_screenSingleplayer, image=retry_button_image,bd = 0)
    main_menu_button = Button(win_screenSingleplayer, image = mainmenuButtonImage,bd= 0)

    backgroundImageWinscreenSingle.grid(row=0,column = 0,columnspan= 55,rowspan= 50)
    retry_button.grid(row = 25,column= 28)
    main_menu_button.grid(row = 28, column = 28)

    def clear_tiles():
        tile1.config(image= tile_image,bg = 'white')
        tile2.config(image= tile_image,bg = 'white')
        tile3.config(image= tile_image,bg = 'white')
        tile4.config(image= tile_image,bg = 'white')
        tile5.config(image= tile_image,bg = 'white')
        tile6.config(image= tile_image,bg = 'white')
        tile7.config(image= tile_image,bg = 'white')
        tile8.config(image= tile_image,bg = 'white')
        tile9.config(image= tile_image,bg = 'white')

    def retry_buttonPressed(a):
        global tiles
        switch_page(single_player)
        clear_tiles()
        tiles = ['tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7', 'tile8', 'tile9']

    def return_to_main_menu(a):
        global tiles
        switch_page(main_menu)
        clear_tiles()
        tiles = ['tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7', 'tile8', 'tile9']



    retry_button.bind("<Button-1>", retry_buttonPressed)
    main_menu_button.bind("<Button-1>", return_to_main_menu)

    def button_click(button):
        global tiles, usedTiles
        default = 'pyimage7'

        def AI_move():
            x = 'pyimage8'
            y = 'pyimage9'
            # Diagonal 1 : stop
            if tile1['image'] == x and tile5['image'] == x and tile9['image'] == default:
                tile9.config(image= o_image)
                tiles.remove('tile9')
            elif tile5['image'] == x and tile9['image'] == x and tile1['image'] == default:
                tile1.config(image = o_image)
                tiles.remove('tile1')
            # Diagonal 2 : stop 3 5 7
            elif tile3['image'] == x and tile5['image'] == x and tile7['image'] == default:
                tile7.config(image = o_image)
                tiles.remove('tile7')

            elif tile7['image'] == x and tile5['image'] == x and tile3['image'] == default:
                tile3.config(image = o_image)
                tiles.remove('tile3')

            elif tile1['image'] == x and tile2['image'] == x and tile3['image'] == default:
                tile3.config(image = o_image)
                tiles.remove('tile3')

            elif tile2['image'] == x and tile3['image'] == x and tile1['image'] == default:
                tile1.config(image = o_image)
                tiles.remove('tile1')

            elif tile4['image'] == x and tile5['image'] == x and tile6['image'] == default:
                tile6.config(image = o_image)
                tiles.remove('tile6')

            elif tile5['image'] == x and tile6['image'] == x and tile4['image'] == default:
                tile4.config(image = o_image)
                tiles.remove('tile4')

            elif tile7['image'] == x and tile8['image'] == x and tile9['image'] == default:
                tile9.config(image = o_image)
                tiles.remove('tile9')

            elif tile8['image'] == x and tile9['image'] == x and tile7['image'] == default:
                tile7.config(image = o_image)
                tiles.remove('tile7')

            elif tile1['image'] == x and tile4['image'] == x and tile7['image'] == default:
                tile7.config(image = o_image)
                tiles.remove('tile7')

            elif tile4['image'] == x and tile7['image'] == x and tile1['image'] == default:
                tile1.config(image = o_image)
                tiles.remove('tile1')

            elif tile5['image'] == x and tile8['image'] == x and tile2['image'] == default:
                tile2.config(image = o_image)
                tiles.remove('tile2')

            elif tile3['image'] == x and tile6['image'] == x and tile9['image'] == default:
                tile9.config(image = o_image)
                tiles.remove('tile9')

            elif tile6['image'] == x and tile9['image'] == x and tile3['image'] == default:
                tile3.config(image = o_image)
                tiles.remove('tile3')

            elif tile1['image'] != 'pyimage7' and tile2['image'] != 'pyimage7' and tile2['image'] != 'pyimage7':
                if tile4['image'] != 'pyimage7' and tile5['image'] != 'pyimage7' and tile6['image'] != 'pyimage7':
                    if tile7['image'] != 'pyimage7' and tile8['image'] != 'pyimage7' and tile9['image'] != 'pyimage7':
                        switch_page(win_screenSingleplayer)
                        backgroundImageWinscreenSingle.config(image = drawImage)

            else:
                move = random.choice(tiles)
                if move == 'tile1' and tile1['image'] == default:
                    tile1.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile1':
                    AI_move()

                if move == 'tile2' and tile2['image'] == default:
                    tile2.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile2':
                    AI_move()

                if move == 'tile3' and tile3['image'] == default:
                    tile3.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile3':
                    AI_move()

                if move == 'tile4' and tile4['image'] == default:
                    tile4.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile4':
                    AI_move()

                if move == 'tile5' and tile2['image'] == default:
                    tile2.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile5':
                    AI_move()

                if  move == 'tile6' and tile6['image'] == default:
                    tile6.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile6':
                    AI_move()

                if move == 'tile7' and tile7['image'] == default:
                    tile7.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile7':
                    AI_move()

                if move == 'tile8' and tile8['image'] == default:
                    tile8.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile8':
                    AI_move()

                if move == 'tile9' and tile9['image'] == default:
                    tile9.config(image = o_image)
                    tiles.remove(move)
                elif move == 'tile9':
                    AI_move()

        if button['image'] == default:
            button.config(image=x_image)
            AI_move()

        def winscrenplayer():
            switch_page(win_screenSingleplayer)
            backgroundImageWinscreenSingle.config(image = you_win)

        def winscreenAI():
            switch_page(win_screenSingleplayer)
            backgroundImageWinscreenSingle.config(image = AI_wins)

        if tile1['image'] == x_placed and tile2['image'] == x_placed and tile3['image'] == x_placed:
            winscrenplayer()
        elif tile4['image'] == x_placed and tile5['image'] == x_placed and tile6['image'] == x_placed:
            winscrenplayer()
        elif tile7['image'] == x_placed and tile8['image'] == x_placed and tile9['image'] == x_placed:
            winscrenplayer()
        elif tile2['image'] == x_placed and tile5['image'] == x_placed and tile8['image'] == x_placed:
            winscrenplayer()
        elif tile1['image'] == x_placed and tile5['image'] == x_placed and tile9['image'] == x_placed:
            winscrenplayer()
        elif tile3['image'] == x_placed and tile5['image'] == x_placed and tile7['image'] == x_placed:
            winscrenplayer()
        elif tile1['image'] == x_placed and tile4['image'] == x_placed and tile7['image'] == x_placed:
            winscrenplayer()
        elif tile2['image'] == x_placed and tile5['image'] == x_placed and tile8['image'] == x_placed:
            winscrenplayer()
        elif tile3['image'] == x_placed and tile6['image'] == x_placed and tile9['image'] == x_placed:
            winscrenplayer()

        if tile1['image'] == y_placed and tile2['image'] == y_placed and tile3['image'] == y_placed:
            winscreenAI()
        elif tile4['image'] == y_placed and tile5['image'] == y_placed and tile6['image'] == y_placed:
            winscreenAI()
        elif tile7['image'] == y_placed and tile8['image'] == y_placed and tile9['image'] == y_placed:
            winscreenAI()
        elif tile2['image'] == y_placed and tile5['image'] == y_placed and tile8['image'] == y_placed:
            winscreenAI()
        elif tile1['image'] == y_placed and tile5['image'] == y_placed and tile9['image'] == y_placed:
            winscreenAI()
        elif tile3['image'] == y_placed and tile5['image'] == y_placed and tile7['image'] == y_placed:
            winscreenAI()
        elif tile1['image'] == y_placed and tile4['image'] == y_placed and tile7['image'] == y_placed:
            winscreenAI()
        elif tile2['image'] == y_placed and tile5['image'] == y_placed and tile8['image'] == y_placed:
            winscreenAI()
        elif tile3['image'] == y_placed and tile6['image'] == y_placed and tile9['image'] == y_placed:
            winscreenAI()


    tile1 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile1))
    tile2 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile2))
    tile3 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile3))
    tile4 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile4))
    tile5 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile5))
    tile6 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile6))
    tile7 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile7))
    tile8 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile8))
    tile9 = Button(single_player, image= tile_image,bd= 0,command = lambda : button_click(tile9))

    def backButtonPressed(back):
        global tiles
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
        tiles = ['tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7', 'tile8', 'tile9']

    def refreshSinglePlayer(a):
        global tiles
        tile1.config(image= tile_image,bg = 'white')
        tile2.config(image= tile_image,bg = 'white')
        tile3.config(image= tile_image,bg = 'white')
        tile4.config(image= tile_image,bg = 'white')
        tile5.config(image= tile_image,bg = 'white')
        tile6.config(image= tile_image,bg = 'white')
        tile7.config(image= tile_image,bg = 'white')
        tile8.config(image= tile_image,bg = 'white')
        tile9.config(image= tile_image,bg = 'white')
        tiles = ['tile1', 'tile2', 'tile3', 'tile4', 'tile5', 'tile6', 'tile7', 'tile8', 'tile9']

    refreshbuttonSinglePlayer = Label(single_player, image=refresingleplayer, bd=0, bg='black')

    backButton.bind('<Button-1>',backButtonPressed)
    refreshbuttonSinglePlayer.bind("<Button-1>",refreshSinglePlayer)

    background_slngle_playeru.grid(rowspan=100,columnspan=100)
    backButton.grid(row = 0,column=0)
    refreshbuttonSinglePlayer.grid(row = 0,column=1,columnspan=6,rowspan= 1)

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
    drawScrene = PhotoImage(file = 'multi_player_image/drawScreen.png')

    background_multiplayer = Label(multi_player, image=playerXTurn, bd=0, bg='black')
    backButton = Label(multi_player, image=backButtonImage, bd=0, bg='black')
    refreshbutton = Label(multi_player, image=refresingleplayer, bd=0, bg='black')

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
