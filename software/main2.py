import os
import sys
import time

import pygame
import serial

import counter

pc = os.uname()[1]

if pc == "raspberrypi":
    from pyrasp import display
    development = False
else:
    development = True


def _exit(signal, frame):
    pygame.quit()
    os._exit(0)


def update_display(display, screen):
    display.set_window()
    # Grab the pygame screen as a bytes object
    pixelbytes = pygame.transform.rotate(screen, 180).convert(16, 0).get_buffer()
    # Lazy (slow) byteswap:
    pixelbytes = bytearray(pixelbytes)
    pixelbytes[::2], pixelbytes[1::2] = pixelbytes[1::2], pixelbytes[::2]
    # Bypass the ST7789 PIL image RGB888->RGB565 conversion
    for i in range(0, len(pixelbytes), 4096):
        display.data(pixelbytes[i:i + 4096])


if development ==False:
    display_1 = display(0, 0)
    display_2 = display(1, 0)
    os.putenv('SDL_VIDEODRIVER', 'dummy')
    pygame.display.init() 
    screen_1 = pygame.Surface((240, 240))
    screen_2 = pygame.Surface((240, 240))


path = "src/img/C/L1/"
imgs = [pygame.image.load(path+"CL1-{:04d}.png".format(i)) for i in range(61)]
running = True



frames = 61
frame = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            break


    # Draw the image
    screen_1.blit(pygame.transform.rotate(imgs[frame],-90), (0, 0))

    update_display(display_1, screen_1)
    if frame == frames:
        frame = 0
    else:
        frame += 1
    time.sleep(0.01)


pygame.quit()
sys.exit(0)

