import tkinter as tk
from gui.tk_constants import *


class DisplayLblFrame(tk.LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.text='Prikaz mjerenja sa senzora'
        
        self.lbl_display_tmp_var = tk.StringVar()
        self.lbl_display_tmp = tk.Label(self,
                    textvariable=self.lbl_display_tmp_var,
                    font=LABEL_HEADER_FONT)
        self.lbl_display_tmp.grid(row=0, column=0,
                              padx=10, pady=10, sticky='ew',
                              ipadx=10, ipady=10)
        
        self.lbl_display_pressure_var = tk.StringVar()
        self.lbl_display_pressure = tk.Label(self,
                    textvariable=self.lbl_display_pressure_var,
                    font=LABEL_HEADER_FONT)
        self.lbl_display_pressure.grid(row=0, column=1,
                              padx=10, pady=10, sticky='ew',
                              ipadx=10, ipady=10)
        
        self.lbl_display_humidity_var = tk.StringVar()
        self.lbl_display_humidity = tk.Label(self,
                    textvariable=self.lbl_display_humidity_var,
                    font=LABEL_HEADER_FONT)
        self.lbl_display_humidity.grid(row=0, column=2,
                              padx=10, pady=10, sticky='ew',
                              ipadx=10, ipady=10)
