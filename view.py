
import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    
    padding = 10

    max_buttons_per_row = 4
    button_captions = [
        '%', 'CE', 'C', '⌫',
        '1/x', 'x²', '√x', '÷',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        '+/-', 0, '.', '='
    ]


    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.value_var = tk.StringVar()
        self.resizable(width=False, height=False)
        self.title("Calculator :3")

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()

    
    def main(self):
        self.mainloop()


    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.padding, pady=self.padding)


    def _make_entry(self):
        ent = ttk.Entry(
            self.main_frame, justify='right', 
            textvariable=self.value_var, state='disabled'
            )
        ent.pack(fill='x')


    def _make_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        buttons_in_row = self.max_buttons_per_row

        for caption in self.button_captions:
            if buttons_in_row == self.max_buttons_per_row:
                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack()
                buttons_in_row = 0
            
            button = ttk.Button(
                inner_frame, text=caption, width=10, 
                command=(lambda button=caption: self.controller.on_button_click(button))
                )
            button.pack(side='left')
            buttons_in_row += 1

