import customtkinter as ctk

from services.sense_services import *



class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title('RPi Python Air Sensors')
        self.geometry('600x400')
        self.grid_columnconfigure(0, weight=1)


        self.btn_refresh = ctk.CTkButton(self,
                            text='Osvjezi mjerenje',
                            command=self.btn_refresh_click)
        self.btn_refresh.grid(row=0, column=0,
                        padx=20, pady=20,
                        sticky='ew')


        self.lbl_temperature_var = ctk.StringVar()
        self.lbl_temperature_var.set('')
        self.lbl_temperature = ctk.CTkLabel(self,
                    textvariable=self.lbl_temperature_var)
        self.lbl_temperature.grid(row=1, column=0,
                            padx=20, pady=20,
                            sticky='ew')

        self.lbl_pressure_var = ctk.StringVar()
        self.lbl_pressure_var.set('')
        self.lbl_pressure = ctk.CTkLabel(self,
                    textvariable=self.lbl_pressure_var)
        self.lbl_pressure.grid(row=2, column=0,
                            padx=20, pady=20,
                            sticky='ew')

        self.lbl_humidity_var = ctk.StringVar()
        self.lbl_humidity_var.set('')
        self.lbl_humidity = ctk.CTkLabel(self,
                    textvariable=self.lbl_humidity_var)
        self.lbl_humidity.grid(row=3, column=0,
                            padx=20, pady=20,
                            sticky='ew')


    def btn_refresh_click(self):
        current_measurement = get_current_measurement()
        self.lbl_temperature_var.set(current_measurement.air_temperature)
        self.lbl_pressure_var.set(current_measurement.air_pressure)
        self.lbl_humidity_var.set(current_measurement.air_humidity)
