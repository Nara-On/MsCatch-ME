import serial
import time
import os
from enum import IntEnum

class ArduinoCommunication:
    COMUNICATION_DELAY = 0.05 # seconds

    def __init__(self):
        port = 'port name is saved here'
        if os.name == 'nt':
            port = 'COM3'           # port on windows in my pc (Erik V)
        elif os.name == 'posix':
            port = '/dev/ttyACM0'   # port on linux by default might have to change this
        else:
            # this shouldn't happen as os.name can only have 'nt' or 'posix' as values
            raise Exception(f"Current OS is not supported, detected OS: {os.name}")
        self.serial = serial.Serial(port, 9600, timeout=1)
        self.serial.flush()

    def send_message(self, message):
        time.sleep(self.COMUNICATION_DELAY)
        if type(message) != bytes:
            self.serial.write(bytes(f'{message}\n', 'utf-8'))
        else:
            self.serial.write(message + b'\n')
        time.sleep(self.COMUNICATION_DELAY)

    def read_message(self):
        lines = []
        while self.serial.in_waiting > 0:
            line = self.serial.readline()
            lines.append(line.strip(b'\r\n'))
            time.sleep(self.COMUNICATION_DELAY)
        return lines

class CatchProtocol:
    # command example
    # 3 bytes
    # SET_MOTOR_X DIRECTION SPEED

    # enums
    class COMMAND(IntEnum):
        SET_MOTOR_1 = 0
        SET_MOTOR_2 = 1
        # N_MOTORS = 2

    class DIRECTIONS(IntEnum):
        # from 'AFMotor.h'
        FORWARD = 1
        BACKWARD = 2
        BREAK = 3       # DOES NOT WORK WITH DC MOTORS
        STOP = 4        # its called RELEASE in the header file
        RELEASE = 4     # same as stop just in case

    class RESPONSES(IntEnum):
        NOT_ENOUGH_CHARACTERS = 0
        TOO_MANY_CHARACTERS = 1

    def command_to_binary(command: COMMAND, direction: DIRECTIONS, speed: int):
        if not (0 <= speed and speed <= 255): raise Exception(f"Invalid speed, must be between 0 and 255, current value is {speed}")
        binary = command.to_bytes(1, 'big') + direction.to_bytes(1, 'big') + speed.to_bytes(1, 'big')

        return binary



if __name__ == '__main__':
    ard_com = ArduinoCommunication()
    # since we power through usb, connecting reboots the arduino and we need to wait for it to start listening
    time.sleep(2)

    # prepare command
    res = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_1, CatchProtocol.DIRECTIONS.BACKWARD, 0)
    res2 = CatchProtocol.command_to_binary(CatchProtocol.COMMAND.SET_MOTOR_2, CatchProtocol.DIRECTIONS.FORWARD, 0)
    print(list(res))

    ard_com.send_message(res)
    ard_com.send_message(res2)
    ret_mess = ard_com.read_message()
    print(ret_mess)
