from datetime import datetime as dt


class AirMeasurement():
    def __init__(self, 
                 air_temperature: float = 0,
                 air_pressure: float = 0,
                 air_humidity: float = 0) -> None:
        self.air_temperature: float = air_temperature
        self.air_pressure: float = air_pressure
        self.air_humidity: float = air_humidity


    def __str__(self):
        to_string = '*****************************************\n'
        to_string += dt.now().strftime('%Y-%m-%d %H:%M:%S\n')
        to_string += f'Temperatura: {self.air_temperature} C\n'
        to_string += f'Tlak: {self.air_pressure} hPa\n'
        to_string += f'Vlaznost: {self.air_humidity} %\n'
        to_string += '*****************************************\n'

        return to_string

    def get_tmp_C(self) -> str:
        return f'{self.air_temperature} C'
    
    def get_tmp_F(self) -> str:
        return f'{round(((self.air_temperature * (9 / 5)) + 32), 2)} F'
    
    def get_pressure(self) -> str:
        return f'{self.air_pressure} hPa'
    
    def get_humidity(self) -> str:
        return f'{self.air_humidity} %'
