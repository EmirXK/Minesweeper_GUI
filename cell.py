from tkinter import *
import tkinter.font as font
import random
import settings
import ctypes
import sys


class Cell:

    all = []
    cell_count = settings.CELL_COUNT - settings.MINES_COUNT
    cell_count_label_object = None
    mark_count = 0
    mark_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.is_checked = False
        self.check_counter = 0
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            bg="gray",
            width=6,
            height=2,
            text="",
        )
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            width=15,
            height=2,
            font=("", 17),
            text=f"Cells Left:{Cell.cell_count}",
        )
        Cell.cell_count_label_object = lbl

    def paint_buttons(self):
        if not self.is_opened and not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="light gray",
            )

        if self.is_opened and not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="light gray",
            )

    @staticmethod
    def create_mark_count_label(location2):
        lbl_2 = Label(
            location2,
            bg="black",
            fg="white",
            width=15,
            height=2,
            font=("", 17),
            text=f"Cells marked:{Cell.mark_count}" + "/" + str(settings.MINES_COUNT),
        )
        Cell.mark_count_label_object = lbl_2

    def left_click_actions(self, event):
        Cell.paint_buttons(self)

        if not self.is_mine_candidate:
            if self.is_mine:
                self.show_mine()
            else:
                self.show_cell()
                if self.surrounded_cells_mines_length == 0:
                    for cell_object in self.surrounded_cells:
                        cell_object.show_cell()
                        if cell_object.surrounded_cells_mines_length == 0 and not self.is_checked:
                            Cell.left_click_actions(cell_object, event)
                            self.is_checked = True

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_individual_cell(self):
        if self.surrounded_cells_mines_length != 0:
            for cell in self.surrounded_cells:
                if cell.surrounded_cells_mines_length != 0:
                    self.is_opened = True

    def show_cell(self):

        if self.cell_count <= 0:
            ctypes.windll.user32.MessageBoxW(0, "Congratulations", "You Win!", 0)
            sys.exit()

        if not self.is_opened:
            Cell.cell_count -= 1

            if self.surrounded_cells_mines_length == 0:
                self.cell_btn_object.configure(
                    bg="light gray",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
                for cell in self.surrounded_cells:
                    self.is_opened = True
                    if cell.surrounded_cells_mines_length == 0:
                        if not cell.is_checked:
                            Cell.show_cell(cell)
                            for cell_object in self.surrounded_cells:
                                cell_object.show_cell()
                                Cell.show_cell(cell_object)
                                Cell.show_individual_cell(cell_object)
                                Cell.show_individual_cell(self)
                            cell.is_checked = True

            if self.surrounded_cells_mines_length == 1:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="blue",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 2:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="green",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 3:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="red",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 4:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="dark blue",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 5:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="brown",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 6:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="cyan",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 7:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="black",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )
            if self.surrounded_cells_mines_length == 8:
                self.cell_btn_object.configure(
                    text=self.surrounded_cells_mines_length,
                    bg="light gray",
                    fg="gray",
                    font=font.Font(
                        size=9,
                        weight="bold"
                    )
                )

            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}",
                )

        self.cell_btn_object.configure(
            bg="light gray"
        )
        self.is_mine_candidate = False
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(
            bg="red"
        )
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", "Game Over", 0)
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_opened:
            if not self.is_mine_candidate:
                self.cell_btn_object.configure(
                    bg="crimson",
                )
                self.is_mine_candidate = True
                Cell.mark_count += 1
                Cell.mark_count_label_object.configure(
                    text=f"Cells marked:{Cell.mark_count}" + "/" + str(settings.MINES_COUNT),
                )
            else:
                self.cell_btn_object.configure(
                    bg="gray",
                )
                self.is_mine_candidate = False
                Cell.mark_count -= 1
                Cell.mark_count_label_object.configure(
                    text=f"Cells marked:{Cell.mark_count}" + "/" + str(settings.MINES_COUNT),
                )

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
