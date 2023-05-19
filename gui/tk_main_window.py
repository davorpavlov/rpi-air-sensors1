import tkinter as tk
from gui.tk_constants import *
from gui.tk_display_lbl_frame import DisplayLblFrame
from services.sense_services import get_current_measurement
from sense_emu import SenseHat

class TkMainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Sense HAT App')
        self.geometry('600x400')
        self.grid_columnconfigure(0, weight=1)

        self.chk_measure_tmp_var = tk.IntVar()
        self.chk_measure_pressure_var = tk.IntVar()
        self.chk_measure_humidity_var = tk.IntVar()

        self.chk_measure_tmp = tk.Checkbutton(
            self,
            text='Mjerenje temperature',
            font=("Arial", 12),
            variable=self.chk_measure_tmp_var
        )
        self.chk_measure_tmp.grid(row=0, column=0,
                                  padx=10, pady=5, sticky='w')

        self.chk_measure_pressure = tk.Checkbutton(
            self,
            text='Mjerenje tlaka',
            font=("Arial", 12),
            variable=self.chk_measure_pressure_var
        )
        self.chk_measure_pressure.grid(row=1, column=0,
                                       padx=10, pady=5, sticky='w')

        self.chk_measure_humidity = tk.Checkbutton(
            self,
            text='Mjerenje vlaÂžznosti',
            font=("Arial", 12),
            variable=self.chk_measure_humidity_var
        )
        self.chk_measure_humidity.grid(row=2, column=0,
                                       padx=10, pady=5, sticky='w')

        self.btn_refresh = tk.Button(
            self,
            text='Osvjezi podatke',
            font=("Arial", 12),
            command=self.btn_refresh_clicked
        )
        self.btn_refresh.grid(row=0, column=1,
                              rowspan=3, padx=20, pady=10,
                              sticky='nsew')

        self.display_text = tk.StringVar()
        self.lbl_display_results = DisplayLblFrame(self)
        self.lbl_display_results.grid(row=3, column=0,
                                      padx=20, pady=20,
                                      sticky='ew', ipadx=20, ipady=20)
        self.lbl_display_results.config(text='Prikaz mjerenja sa senzora')
    def btn_refresh_clicked(self):
        sense = SenseHat()

        measurements = {
            "Temperatura": (self.chk_measure_tmp_var, sense.get_temperature, "Â°C"),
            "Tlak": (self.chk_measure_pressure_var, sense.get_pressure, "hPa"),
            "Vlaznost": (self.chk_measure_humidity_var, sense.get_humidity, "%")
        }

        display_text = ""
        for measurement, (var, func, unit) in measurements.items():
            if var.get() == 1:
                value = func()
                display_text += f"{measurement}: {value:.2f} {unit}\n"

        self.lbl_display_results.lbl_display_tmp_var.set("")
        self.lbl_display_results.lbl_display_pressure_var.set("")
        self.lbl_display_results.lbl_display_humidity_var.set("")

        self.lbl_display_results.lbl_display_tmp_var.set(display_text)
