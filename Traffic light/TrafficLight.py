from machine import Pin
import time

class Led:
    def __init__(self, ledColor, valueNumber, timeLength=0):
        self.ledColor = ledColor
        self.valueNumber = valueNumber
        self.timeLength = timeLength
      
    def on_off(self):
        self.ledColor.value(self.valueNumber), time.sleep(self.timeLength)
    
    @classmethod
    def all_off(cls, color_dict):
        for color in color_dict.values():
            cls(color, 0).on_off()

ledColor_dict = {
    "ledR" : Pin(17, Pin.OUT),
    "ledY" : Pin(15, Pin.OUT), 
    "ledG" : Pin(14, Pin.OUT)
}

Led.all_off(ledColor_dict)

try:
    mode = int(input('Enter a mode: '))
    if mode == 1:      
        while True:
            Led(ledColor_dict["ledY"], 1, 1).on_off()
            Led(ledColor_dict["ledY"], 0, 1).on_off()
        
    elif mode == 2:
        redTime = int(input('Enter time length of red light: '))
        greenTime = int(input('Enter time length of green light: '))
        while True:
            Led(ledColor_dict["ledR"], 1, redTime).on_off()
            
            Led(ledColor_dict["ledY"], 1, 2).on_off()
            Led(ledColor_dict["ledY"], 0).on_off()
            Led(ledColor_dict["ledR"], 0).on_off()

            Led(ledColor_dict["ledG"], 1, greenTime).on_off()
            Led(ledColor_dict["ledG"], 0).on_off()
            
            Led(ledColor_dict["ledY"], 1, 2).on_off()
            Led(ledColor_dict["ledY"], 0).on_off()

    else:
        Led.all_off(ledColor_dict)
        print("Please should only mode 1 or 2!!!")
        
except KeyboardInterrupt:    
    Led.all_off(ledColor_dict)
    print("Program terminated by user.")