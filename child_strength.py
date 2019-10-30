import RPi.GPIO as gpio

# Physical pin number
PIN = 2

# Define board layout
gpio.setmode(gpio.BCM)

# Define pin as input
gpio.setup(PIN, gpio.IN)

# Write data to specified file
def write_to_file(data):
    with open("./data.txt", "a") as f:
        f.write(data)

# Control loop to gather pin data
while True:
    if gpio.input(PIN):
        print("test")
        write_to_file("datadata\n")
