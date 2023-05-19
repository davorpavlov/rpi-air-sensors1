import tkinter as tk
from gui.tk_constants import *
from gui.tk_display_lbl_frame import DisplayLblFrame
from services.sense_services import get_current_measurement


class TkMainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Tkinter RPi App')
        self.geometry('600x400')
        self.grid_columnconfigure(0, weight=1)


        self.btn_refresh = tk.Button(self,
                                     text='Osvjezi podatke',
                                     font=BUTTON_FONT,
                                     command=self.btn_refresh_clicked)
        self.btn_refresh.grid(row=0, column=0,
                              padx=20, pady=10, sticky='ew',
                              ipadx=20, ipady=20)


        self.lfrm_display_results = DisplayLblFrame(self)
        self.lfrm_display_results.grid(row=1, column=0,
                              padx=20, pady=10, sticky='ew',
                              ipadx=20, ipady=20)


    def btn_refresh_clicked(self):
        current_measurement = get_current_measurement()
        self.lfrm_display_results.lbl_display_tmp_var.set(
            current_measurement.get_tmp_C()
        )
        
        self.lfrm_display_results.lbl_display_pressure_var.set(
            current_measurement.get_pressure()
        )
        
        self.lfrm_display_results.lbl_display_humidity_var.set(
            current_measurement.get_humidity()
        )
