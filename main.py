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

    def pressed_on_singleplayer():
        pass

    def pressed_on_multiplayer():
        pass

    def pressed_on_exit(exit):
        window.destroy()

    exit_button.bind("<Button-1>", pressed_on_exit)

    window.geometry('722x600')
    window.mainloop()

if __name__ == '__main__':
    main()
