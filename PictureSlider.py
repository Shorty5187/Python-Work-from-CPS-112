from tkinter import *
from PIL import Image, ImageTk
import random

 #tkinter canvas documentation:    effbot.org/tag/Tkinter.Canvas

class TKImageTile:

    def __init__(self, file_name, max_width, max_height, rows, cols, gap=0):

        self.rows = rows
        self.cols = cols
        self.gap = gap
        self.image = Image.open('images\\Ducks.jpg')#change the file name to a picture that you have
        print(self.image)

        self.img_width = max_width

        scale = self.img_width / self.image.width
        self.img_height = int(self.image.height * scale)

        self.cell_width = int(self.img_width/self.cols) #keeps track of each cell so you don't have to calculate it each time.
        self.cell_height = int(self.img_height/self.rows) #keeps track of each cell so you don't have to calculate it each time.

        self.image = self.image.resize( (self.img_width, self.img_height), Image.LANCZOS)
        print(self.image.width, self.image.height)

    def get_tk_image(self, row, col): #cuts the picture into specific sections
        crop_img = self.image.crop((self.x(col),self.y(row),self.x(col+1)- self.gap, self.y(row+1)- self.gap ))
        return ImageTk.PhotoImage(crop_img)

    def x(self, col):
        return col * self.cell_width

    def y(self, row):
        return row * self.cell_height

class PuzzleTile:

    #class variable because it adjusts to how many collectivley shared
    id_to_rowcol = {}
    #class variable: maps row, col to corresponding puzzle tiles
    #row_col_to_id = None
    rowcol_to_tile = None

    #initalizes row x col grid
    @classmethod
    def set_rows_cols(cls, rows, cols):
       cls.rowcol_to_tile = [[None for c in range(cols)]for r in range(rows)]#serves as a placeholder

    @classmethod
    def get_puzzle_by_id(cls, img_id):
        return PuzzleTile.id_to_rowcol[img_id]

    def __init__(self, row, col, canvas, tk_image_tiles, event_function):
        self.row = row
        self.col = col

        self.tk_image = tk_image_tiles.get_tk_image(row, col)

        self.image_id = canvas.create_image(tk_image_tiles.x(col), tk_image_tiles.y(row), image = self.tk_image, anchor=NW)
        print(self.image_id)

        PuzzleTile.id_to_rowcol[self.image_id] = self
        #PuzzleTile.rowcol_to_tile[row][col]

        canvas.tag_bind(self.image_id, '<Button-1>', event_function)

    #copies image from "from_tile' to self.
    # def copy_image(self, from_tile):
    #     from_tile = self.rowcol_to_tile
    #     self.copy_image()

    def blank_image(self):
        canvas.itemconfigure(self.image_id, image = '')
        self.tk_image = None

    #moves the blank that is at "other" to "self"
    def move_to(self, other):
        canvas.itemconfigure(other.image_id, image = self.tk_image)
        other.tk_image = self.tk_image
        self.blank_image()

    #is other next to self? (returns True/False)
    def is_neighbor(self, other, valid_move):
        self.valid_move = valid_move
        if self.row == other.row and other.col ==self.col -1:
            return valid_move
        elif self.row == other.row and other.col == self.col +1:
            return valid_move
        elif self.col == other.col and other.row == self.row -1:
            return valid_move
        elif self.col == other.col and other.row == self.row +1:
            return valid_move
        else:
            return False

# -- Main Program--
def init_screen():
    global tk, canvas, ROWS, COLS, blank_tile #have to keep an image around

    ROWS, COLS = 3, 4
    tk = Tk()
    tk.title("Picture Slider")

    tk.resizable(False, False)

    tk_image_tiles = TKImageTile("image/Ducks.jpg", 800, 600, ROWS, COLS, 1)

    canvas = Canvas(tk, width=tk_image_tiles.img_width, height=tk_image_tiles.img_height)
    canvas.pack()

    PuzzleTile.set_rows_cols(ROWS, COLS)
    #print( PuzzleTile.rowcol_to_tile)

    for row in range(ROWS):
        for col in range(COLS):
            tile = PuzzleTile(row, col, canvas, tk_image_tiles, tile_click)

    blank_tile = tile
    blank_tile.blank_image()

def tile_click(event):
    global blank_tile
    cur_id = canvas.find_withtag(CURRENT)[0]
    print("ouch", cur_id)

    clicked_tile = PuzzleTile.id_to_rowcol[cur_id]
    print(clicked_tile.row, clicked_tile.col)
    print(blank_tile.row, blank_tile.col)
    clicked_tile.move_to(blank_tile)
    blank_tile = clicked_tile

def shuffle():
    global blank_puzzle, tk_image_tiles

    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)

    directions = [up, right, down, left]

    for i in range(ROWS*COLS*10):
        #find a valid direction to move
        while True:
            off_row, off_col = directions[random.randint(0, 3)]

            next_row = blank_puzzle.row + off_row
            next_col = blank_puzzle.col + off_col

            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                break

        next_puzzle = PuzzleTile.rowcol_to_tile[next_row][next_col]
        next_puzzle = PuzzleTile.get_puzzle_by_id[next_row, next_col]
        next_puzzle.move_to(blank_tile)

init_screen()

mainloop()
