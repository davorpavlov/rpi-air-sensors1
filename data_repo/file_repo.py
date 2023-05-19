


def save_to_file(data):
    with open('data_storage/rpi_air_measurements.txt', 'a') as file_writer:
        file_writer.write(str(data))

