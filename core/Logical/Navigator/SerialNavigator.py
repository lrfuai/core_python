from AbstractNavigator import AbstractNavigator;
from serial import Serial;

class SerialNavigator(AbstractNavigator):
    
    FORWARD = "Forward";
    BACKWARD ="Backward";
    LEFT = "Left";
    RIGHT = "Right";

    __movements = { FORWARD : '1', BACKWARD: '2', LEFT : '3', RIGHT: '4' };
    __serial = None;

    @classmethod
    def __init__(self, com, baudRate, dataBits):
        self.__serial = Serial( com-1, baudRate, dataBits);
        self.__serial.close();
        self.__serial.open();

    @classmethod
    def moveForward(self):
        self.__serial.write(self.__movements[self.FORWARD]);
    
    @classmethod
    def moveBackward(self):
        self.__serial.write(self.__movements[self.BACKWARD]);
    
    @classmethod
    def turnLeft(self):
        self.__serial.write(self.__movements[self.LEFT]);

    @classmethod
    def turnRight(self):
        self.__serial.write(self.__movements[self.RIGHT]);