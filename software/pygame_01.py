#!/usr/bin/env python3
import os
import sys
import signal
import pygame
import time
import math
import ST7789



def _exit(sig, frame):
    global running
    running = False
    print("\nExiting!...\n")


def update_display():
    display_hat.set_window()
    display_hat2.set_window()
    # Grab the pygame screen as a bytes object
    pixelbytes = pygame.transform.rotate(screen, 180).convert(16, 0).get_buffer()
    # Lazy (slow) byteswap:
    pixelbytes = bytearray(pixelbytes)
    pixelbytes[0::2], pixelbytes[1::2] = pixelbytes[1::2], pixelbytes[0::2]
    # Bypass the ST7789 PIL image RGB888->RGB565 conversion
    for i in range(0, len(pixelbytes), 4096):
        data = pixelbytes[i:i + 4096]
        display_hat.data(data)
        display_hat2.data(data)




display_hat = ST7789.ST7789(
    height = 240,
    rotation =90,
    port=0,
    cs=0,
    dc=9,
    spi_speed_hz=96*1000*1000,
    offset_left=0,
    offset_top=0
)

display_hat2 = ST7789.ST7789(
    height = 240,
    rotation =90,
    port=1,
    cs=0,
    dc=12,
    spi_speed_hz=96*1000*1000,
    offset_left=0,
    offset_top=0
)

img = pygame.image.load("img.bmp")

os.putenv('SDL_VIDEODRIVER', 'dummy')
pygame.display.init()  # Need to init for .convert() to work
screen = pygame.Surface((240, 240))

signal.signal(signal.SIGINT, _exit)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            break

    # Clear the screen
    #screen.fill((0, 0, 0))

    # Draw the image
    screen.blit(img, (0, 0))

    update_display()
    time.sleep(0.01)


pygame.quit()
sys.exit(0)
