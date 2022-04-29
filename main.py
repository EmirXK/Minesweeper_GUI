from tkinter import *
from cell import Cell
import functions
import settings


root = Tk()

root.title("Minesweeper")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(width=False, height=False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=functions.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper",
    font=("", 48)
)

game_title.place(
    x=functions.width_prct(23),
    y=0,
)

center_frame = Frame(
    root,
    bg="gray",
    width=functions.width_prct(75),
    height=functions.height_prct(75)
)
center_frame.place(x=0, y=functions.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            row=x,
            column=y
        )
Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=100
)

Cell.create_mark_count_label(top_frame)
Cell.mark_count_label_object.place(
    x=450,
    y=100
)


Cell.randomize_mines()

root.mainloop()
