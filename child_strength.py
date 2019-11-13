import pygame
import pyautogui
import RPi.GPIO as gpio
from datetime import datetime

### PyGame ####
# Control loop
running = True

# Game clock 
clock = pygame.time.Clock()
FPS = 40

# LCD screen dimensions
DISPLAY_WIDTH, DISPLAY_HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Initialize game
pygame.init()

# Fonts
small_font = pygame.font.SysFont("quicksand", 20)
large_font = pygame.font.SysFont("quicksand", 64)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
RED = (255, 0, 0)

### RPi.GPIO ###
# Physical pin numbers
GRIP = 1
PULL = 2

# Define board layout
gpio.setmode(gpio.BCM)

# Define pin as input
gpio.setup(GRIP, gpio.IN)
gpio.setup(PULL, gpio.IN)

# Write data to specified file
def write_to_file(data):
    with open("/home/pi/Child_Strength/data.txt", "a") as f:
        f.write(data)

# Control loop
while running:
    
    ### Logic ###
    active_sensor = ""
    sensor_value = "0"

    # Data to send to file
    ll = datetime.now().strftime("%Y,%m%d,%H,%M,%S")

    # Checking Gpio pins
    if gpio.input(GRIP):
        active_sensor = "Gripping"
        sensor_value = str(gpio.input(GRIP))
        ll += " " + active_sensor + ":" + sensor_value
    else:
        active_sensor = "Gripping"
        ll += " " + active_sensor + ":" + sensor_value

    if gpio.input(PULL):
        active_sensor = "Pulling"
        sensor_value = str(gpio.input(PULL))
        ll += " " + active_sensor + ":" + sensor_value
    else:
        active_sensor = "Pulling"
        ll += " " + active_sensor + ":" + sensor_value

    ll += "\n"
    write_to_file(ll)

    ### Drawing ###
    # Screen Clear
    screen.fill(BLACK)

    # Active Sensor String
    sensor_text = large_font.render(active_sensor, False, WHITE)
    screen.blit(sensor_text, ((DISPLAY_WIDTH / 2) - (sensor_text.get_rect().width / 2), (DISPLAY_HEIGHT / 2 - 100) - (sensor_text.get_rect().height / 2)))

    # Sensor Value String
    value_text = large_font.render(sensor_value, False, WHITE)
    screen.blit(value_text, ((DISPLAY_WIDTH / 2) - (value_text.get_rect().width), (DISPLAY_HEIGHT / 2 + 50) - (value_text.get_rect().height / 2)))
    
    # Exit Button
    exit_rect = pygame.draw.rect(screen, RED, (DISPLAY_WIDTH - 22, 2, 20, 20))
    exit_text = small_font.render("X", True, WHITE)
    exit_text_rect = exit_text.get_rect()
    exit_text_rect.center = exit_rect.center
    screen.blit(exit_text, exit_text_rect)

    ### Event System ###
    for event in pygame.event.get():

        # Window Exit
        if event.type == pygame.QUIT:
            running = False

        # ESC Exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Exit Button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            if exit_rect.collidepoint(mouse_pos):
                running = False

    # Update screen
    pygame.display.update()

    # Define FPS
    clock.tick(FPS)

# Exit game
pygame.quit()









