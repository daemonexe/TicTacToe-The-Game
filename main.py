from tkinter import *
from tkinter import PhotoImage

def main():
    window = Tk()
    window.title('TicTacToe - The Game')
    window.resizable(height= False, width= False)
    # Pages :
    main_menu = Frame(window)
    single_player  = Frame(window)
    multi_player = Frame(window)

    # Page switcher
    def switch_page(frame):
        frame.tkraise()

    # Arranging all frames
    for frames in (main_menu,single_player,multi_player):
        frames.grid(row=0, column=0, sticky='news')

    switch_page(main_menu)

    # Images
    main_menu_image = PhotoImage(file = 'main_menu_imgs/main_menu_image.png')
    single_player_button_img = PhotoImage(file = 'main_menu_imgs/singleplayer_button.png')
    multi_player_button_img = PhotoImage(file= 'main_menu_imgs/multiplayer_image.png' )
    exit_button_img = PhotoImage(file= 'main_menu_imgs/exit_image.png')
    singlePlayerImage = PhotoImage(file = 'single_player_imgs/single_player_background.png')
    backButtonImage = PhotoImage(file= 'single_player_imgs/backButtonImage.png')
    tile_image = PhotoImage(file = 'single_player_imgs/x_x.png')

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

    # ----------------------- SINGLE PLAYER -------------------------------
    background_slngle_playeru = Label(single_player,image = singlePlayerImage, bd = 0, bg = 'black')
    backButton = Label(single_player, image = backButtonImage,bd = 0,bg = 'black')

    tile1 = Label(single_player, image= tile_image,bd= 0)
    tile2 = Label(single_player, image= tile_image,bd= 0)
    tile3 = Label(single_player, image= tile_image,bd= 0)
    tile4 = Label(single_player, image= tile_image,bd= 0)
    tile5 = Label(single_player, image= tile_image,bd= 0)
    tile6 = Label(single_player, image= tile_image,bd= 0)
    tile7 = Label(single_player, image= tile_image,bd= 0)
    tile8 = Label(single_player, image= tile_image,bd= 0)
    tile9 = Label(single_player, image= tile_image,bd= 0)


    # functions
    def backButtonPressed(back):
        switch_page(main_menu)

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

    background_multiplayer = Label(multi_player, image=singlePlayerImage, bd=0, bg='black')
    backButton = Label(multi_player, image=backButtonImage, bd=0, bg='black')

    _tile1 = Label(multi_player, image=tile_image, bd=0)
    _tile2 = Label(multi_player, image=tile_image, bd=0)
    _tile3 = Label(multi_player, image=tile_image, bd=0)
    _tile4 = Label(multi_player, image=tile_image, bd=0)
    _tile5 = Label(multi_player, image=tile_image, bd=0)
    _tile6 = Label(multi_player, image=tile_image, bd=0)
    _tile7 = Label(multi_player, image=tile_image, bd=0)
    _tile8 = Label(multi_player, image=tile_image, bd=0)
    _tile9 = Label(multi_player, image=tile_image, bd=0)

    # functions
    def backButtonPressed(back):
        switch_page(main_menu)

    background_multiplayer.grid(rowspan=100, columnspan=100)
    backButton.grid(row=0, column=0)
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

    window.geometry('722x600')
    window.mainloop()

if __name__ == '__main__':
    main()
