import RPi.GPIO as gpio

class Pin: 
    
    def __init__(self, number, name, pullupdown):
        self.number = number
        self.name = name
        self.value = 0
        self.pullupdown = pullupdown

        if self.pullupdown:
            gpio.setup(number, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        else:
            gpio.setup(number, gpio.IN)

    def read_data(self):
        self.value = gpio.input(self.number)
