from tkinter import *
from tkinter import PhotoImage

def main():
    window = Tk()
    window.title('TicTacToe - The Game')
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

    # Images
    main_menu_image = PhotoImage(file = 'main_menu_image.png')
    # Lables
    background_main_menu = Label(image = main_menu_image, bd = 0, bg = 'black')
    # Gridding
    background_main_menu.grid(row = 0,column = 0)

    window.geometry('722x600')
    window.mainloop()

if __name__ == '__main__':
    main()
