from sense_emu import SenseHat

from models.air_measurements import *


sense = SenseHat()


def get_current_measurement() -> AirMeasurement:
    air_temperature = round(sense.get_temperature(), 2)
    air_pressure = round(sense.get_pressure(), 2)
    air_humidity = round(sense.get_humidity(), 2)

    current_measurement = AirMeasurement(
        air_temperature=air_temperature,
        air_pressure=air_pressure,
        air_humidity=air_humidity
    )

    return current_measurement
