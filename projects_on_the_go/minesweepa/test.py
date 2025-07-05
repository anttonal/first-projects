"""
COMP.CS.100 Programming 1 - round 13.
Names: Antton Alivuotila - Johan Nygård
Student IDs: 151259218 - 151394568
Email: antton.alivuotila@tuni.fi - johan.nygård@tuni.fi

Assignment: Minesweeper
"""

from tkinter import *
import random

TILE_BUT_DICT = {}
# picture files for a flag and a bomb


class Menu:

    def __init__(self):
        self.__root = Tk()
        self.__root.configure(bg="#FFFFFF")

        self.__canvas = Canvas(self.__root, width=600, height=300, bg="#FFFFFF")
        self.__frame1 = LabelFrame(self.__root, pady=5, padx=15, bd=0, bg="#FFFFFF")
        self.__frame2 = LabelFrame(self.__root, pady=5, padx=15, bd=0, bg="#FFFFFF")
        self.__frame3 = LabelFrame(self.__root, pady=5, padx=15, bd=0, bg="#FFFFFF")
        self.__frame4 = LabelFrame(self.__root, pady=5, padx=15, bd=0, bg="#FFFFFF")
        self.__titlephoto = PhotoImage(file="titlewithtext.gif")
        self.__title = Label(self.__canvas, image=self.__titlephoto, bg="#FFFFFF")

        self.__beginner_button = Button(self.__frame1, text="Beginner", bg="#90EE90", fg="#FFFFFF",
                                        padx=25, pady=25, font=("Arial Bold", 20), command=self.beginner_game)
        self.__medium_button = Button(self.__frame2, text="Medium", bg="#FFCE30", fg="#FFFFFF",
                                      padx=25, pady=25, font=("Arial Bold", 20), command=self.medium_game)
        self.__expert_button = Button(self.__frame3, text="Expert", bg="#E83845", fg="#FFFFFF",
                                      padx=25, pady=25, font=("Arial Bold", 20), command=self.expert_game)
        self.__quit_button = Button(self.__frame4, text="Quit", bg="#AAAAAA", fg="#FFFFFF", command=self.quit_game)

        self.__canvas.grid(row=0, column=0, columnspan=3)
        self.__frame1.grid(row=1, column=0)
        self.__frame2.grid(row=1, column=1)
        self.__frame3.grid(row=1, column=2)
        self.__frame4.grid(row=2, column=1)
        self.__title.pack()
        self.__beginner_button.pack()
        self.__medium_button.pack()
        self.__expert_button.pack()
        self.__quit_button.pack()

        self.__root.mainloop()

    def quit_game(self):
        self.__root.destroy()

    def beginner_game(self):
        self.quit_game()
        mine_tiles, empty_tiles = create_field([8, 8], 10)
        Board(mine_tiles, empty_tiles)

    def medium_game(self):
        self.quit_game()
        mine_tiles, empty_tiles = create_field([16, 16], 40)
        Board(mine_tiles, empty_tiles)

    def expert_game(self):
        self.quit_game()
        mine_tiles, empty_tiles = create_field([16, 30], 99)
        Board(mine_tiles, empty_tiles)


class Board:

    def __init__(self, mines, empty_tiles):
        self.__root = Tk()

        self.__mines = mines
        self.__empty_tiles = empty_tiles

        self.__root.configure(bg="white", relief="flat", borderwidth=10)

        self.__reset_img = PhotoImage(file="neutralface.gif")

        # Creating all components in the GUI
        self.__visuals_frame = LabelFrame(self.__root, relief="sunken", borderwidth=10)
        self.__field_frame = LabelFrame(self.__root, relief="sunken", borderwidth=10)
        self.__restart_button = Button(self.__visuals_frame, image=self.__reset_img, command=self.restart)
        self.__flag_count = Label(self.__visuals_frame, text=f" {len(mines):03d} ", font=("Cambria", 26))
        self.__timer = Label(self.__visuals_frame, text=" TIME ", font=("Cambria", 26))

        for tile in self.__mines:
            TILE_BUT_DICT[tile] = Button(self.__field_frame, padx=10, pady=1, borderwidth=3, command=self.gameover)
            TILE_BUT_DICT[tile].grid(row=tile.getrow(), column=tile.getcol())

        for tile in self.__empty_tiles:
            TILE_BUT_DICT[tile] = Button(self.__field_frame, padx=10, pady=1, borderwidth=3, command=tile.pressed)
            TILE_BUT_DICT[tile].grid(row=tile.getrow(), column=tile.getcol())

        # Attaching all the components to the GUI
        self.__flag_count.pack(side="left")
        self.__restart_button.pack(side="left", expand=True)
        self.__timer.pack(side="right")

        self.__visuals_frame.grid(row=0, sticky=W + E)
        self.__field_frame.grid(row=1)

        self.__root.mainloop()

    def gameover(self):
        self.__reset_img.configure(file="sadface.gif")
        for key in TILE_BUT_DICT:
            if key.ismine:
                TILE_BUT_DICT[key].configure(state="disabled", relief="flat", text="B")

    def gettile(self):
        pass

    def restart(self):
        self.__root.destroy()
        Menu()

    def button_pressed(self):
        tile = self


class Tile:

    def __init__(self, row_column, mine_tiles):

        self.__row = row_column[0]
        self.__column = row_column[1]
        self.__clicked = False
        self.__adjacent = 0
        TILE_BUT_DICT[self] = None

        if row_column in mine_tiles:
            self.__type_mine = True

        else:
            self.__type_mine = False

            for row in range(row_column[0] - 1, row_column[0] + 1):
                for column in range(row_column[1] - 1, row_column[1] + 1):
                    if (row, column) in mine_tiles:
                        self.__adjacent += 1

    def getrow(self):
        return self.__row

    def getcol(self):
        return self.__column

    def ismine(self):
        return self.__type_mine

    def pressed(self):
        if self.__type_mine:
            return
        else:
            TILE_BUT_DICT[self].configure(state="disabled", relief="flat", text="E")


def create_field(dimensions, mine_amount):
    rows = int(dimensions[0])
    cols = (dimensions[1])
    mine_set = set()
    empty_tile_set = set()

    while len(mine_set) < mine_amount:
        coordinate = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        mine_set.add(coordinate)

    for i in range(rows):
        for j in range(cols):
            coordinate = (i, j)
            empty_tile_set.add(coordinate)

    empty_tile_set -= mine_set

    mines = [Tile(xy, mine_set) for xy in mine_set]
    empty_tiles = [Tile(xy, mine_set) for xy in empty_tile_set]

    return mines, empty_tiles


def main():
    Menu()


if __name__ == "__main__":
    main()
