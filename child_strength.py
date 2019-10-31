import pygame
import pyautogui
import RPi.GPIO as gpio

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

# Control loop
while running:
    ### Logic ###
    active_sensor = ""

    # Checking Gpio pins
    if gpio.input(PIN):
        active_sensor = "Sensor X"
        #write_to_file("datadata\n")

    ### Drawing ###

    # Screen Clear
    screen.fill(BLACK)

    # Sensor String
    sensor_text = large_font.render(active_sensor, False, WHITE)
    screen.blit(sensor_text, ((DISPLAY_WIDTH / 2) - (sensor_text.get_rect().width / 2), (DISPLAY_HEIGHT / 2) - (sensor_text.get_rect().height / 2)))

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









