import tkinter as tk

from datetime import datetime


class BinaryClock(tk.Frame):

    BITMAP_OFF = 'gray12'
    BITMAP_ON = 'gray75'
    COLUMN_DAY = 2
    COLUMN_HOUR = 5
    COLUMN_MINUTE = 6
    COLUMN_MONTH = 1
    COLUMN_SECOND = 7
    COLUMN_YEAR = 0
    COLUMNS = [COLUMN_YEAR, COLUMN_MONTH, COLUMN_DAY, COLUMN_HOUR, COLUMN_MINUTE, COLUMN_SECOND]
    GRID_SIZE = 8
    TICK_DELAY_MILLIS = 1000
    YEAR_OFFSET = 2000

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.cells = []
        self.pack()
        self.create_clock()

    def create_clock(self):
        for i in range(self.GRID_SIZE):
            cells = []
            column = tk.Frame()
            for j in range(self.GRID_SIZE):
                button = tk.Button(column, bitmap=self.BITMAP_OFF)
                button.pack(side='top')
                cells.append(button)
            column.pack(side='left')
            self.cells.append(cells)

    def tick(self):
        now = datetime.now()
        fields = [now.year - self.YEAR_OFFSET, now.month, now.day, now.hour, now.minute, now.second]
        for i, value in zip(self.COLUMNS, fields):
            for j in range(self.GRID_SIZE):
                mask = 2 ** j
                new_bitmap = self.BITMAP_ON if value & mask else self.BITMAP_OFF
                self.cells[i][self.GRID_SIZE - 1 - j]['bitmap'] = new_bitmap
        self.after(self.TICK_DELAY_MILLIS, self.tick)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Binary Clock')
    clock = BinaryClock(master=root)
    clock.tick()
    clock.mainloop()

