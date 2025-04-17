#!/usr/bin/env python3
"""Interactive Snake game on iDotMatrix LED matrix."""
import asyncio
import curses
import os
import sys
import random
import pygame
from idotmatrix import ConnectionManager, Graffiti, Text, Gif
from utils.utils import digits

async def snake_game(address, width=32, height=32, speed=0.2, wrap=True):
    # initialize pygame for joystick support
    pygame.init()
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    else:
        print("No joystick detected, using keyboard controls.")
    # connect to device
    conn = ConnectionManager()
    if address.lower() == 'auto':
        await conn.connectBySearch()
    else:
        await conn.connectByAddress(address)
    graffiti = Graffiti()

    # init curses for input
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    curses.noecho()

    # initial snake and apple
    direction = (1, 0)
    snake = [(width // 2, height // 2)]
    snake_length = 3
    apple = None
    # place first apple
    while True:
        pos = (random.randrange(width), random.randrange(height))
        if pos not in snake:
            apple = pos
            await graffiti.setPixel(x=apple[0], y=apple[1], r=255, g=0, b=0)
            break

    # keep a baseline to scale speed as snake grows
    base_speed = speed
    try:
        while True:
            # handle input from joystick or keyboard
            pygame.event.pump()
            new_dir = None
            if joystick:
                # try hat control if available, avoid invalid hat error
                if joystick.get_numhats() > 0:
                    hat = joystick.get_hat(0)
                    if hat[0] != 0 or hat[1] != 0:
                        new_dir = (hat[0], -hat[1])
                # fallback to analog axes if no hat input
                if new_dir is None:
                    x_axis = joystick.get_axis(0)
                    y_axis = joystick.get_axis(1)
                    threshold = 0.5
                    if abs(x_axis) > abs(y_axis) and abs(x_axis) > threshold:
                        new_dir = (1 if x_axis > 0 else -1, 0)
                    elif abs(y_axis) > threshold:
                        new_dir = (0, 1 if y_axis > 0 else -1)
                # quit if joystick button 0 pressed
                if joystick.get_button(0):
                    break
            else:
                key = stdscr.getch()
                if key in (ord('q'), 27):  # quit on 'q' or ESC
                    break
                if key == curses.KEY_UP:
                    new_dir = (0, -1)
                elif key == curses.KEY_DOWN:
                    new_dir = (0, 1)
                elif key == curses.KEY_LEFT:
                    new_dir = (-1, 0)
                elif key == curses.KEY_RIGHT:
                    new_dir = (1, 0)
            # only apply if not reversing
            if new_dir and new_dir != (-direction[0], -direction[1]):
                direction = new_dir

            head = snake[-1]
            # calculate next head position
            new_x = head[0] + direction[0]
            new_y = head[1] + direction[1]
            if wrap:
                new_x %= width
                new_y %= height
            else:
                if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                    break
            new_head = (new_x, new_y)
            # check collision
            if new_head in snake:
                break

            snake.append(new_head)
            # draw new head
            await graffiti.setPixel(x=new_head[0], y=new_head[1], r=0, g=255, b=0)

            # handle apple
            if new_head == apple:
                snake_length += 1
                # place new apple
                while True:
                    pos = (random.randrange(width), random.randrange(height))
                    if pos not in snake:
                        apple = pos
                        await graffiti.setPixel(x=apple[0], y=apple[1], r=255, g=0, b=0)
                        break
            else:
                # remove tail
                if len(snake) > snake_length:
                    tail = snake.pop(0)
                    await graffiti.setPixel(x=tail[0], y=tail[1], r=0, g=0, b=0)

            # adjust speed: decrease delay as snake grows, min 0.05s
            current_speed = max(0.05, base_speed - (snake_length - 3) * 0.01)
            await asyncio.sleep(current_speed)
    finally:
        # clear only the snake pixels before showing score
        for x_pixel, y_pixel in snake:
            await graffiti.setPixel(x=x_pixel, y=y_pixel, r=0, g=0, b=0)
        # also clear the apple pixel
        await graffiti.setPixel(x=apple[0], y=apple[1], r=0, g=0, b=0)
        # display final score on LED using utils.digits
        score = snake_length - 3
        # draw each digit pattern on the LED
        for idx, ch in enumerate(str(score)):
            pattern = digits[ch]
            x_offset = idx * (len(pattern[0]) + 1)
            for y, row in enumerate(pattern):
                for x, pixel in enumerate(row):
                    if pixel == '1':
                        await graffiti.setPixel(x=x_offset + x, y=y, r=0, g=255, b=0)
        # pause so player can see result
        await asyncio.sleep(3)
        # cleanup curses and console message
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        print(f"Game Over. Your score: {score}")
        # display end-game GIF animation
        gif = Gif()
        await gif.uploadUnprocessed(file_path=os.path.join("images", "snake.gif"))
        # disconnect
        try:
            await conn.disconnect()
        except Exception:
            pass

async def main():
    address = os.environ.get('IDOTMATRIX_ADDRESS')
    if not address:
        print('Please set IDOTMATRIX_ADDRESS environment variable (or use "auto").')
        sys.exit(1)
    # console-based options
    speed_input = input("Game speed (seconds per move) [0.1]: ") or "0.1"
    size_input = input("Board size (16 or 32) [32]: ") or "32"
    wrap_input = input("Wrap around edges? (y/n) [y]: ") or "y"
    try:
        speed = float(speed_input)
    except ValueError:
        speed = 0.2
    try:
        size = int(size_input)
        if size not in (16, 32):
            size = 32
    except ValueError:
        size = 32
    wrap = wrap_input.lower() in ('y', 'yes')

    await snake_game(address, width=size, height=size, speed=speed, wrap=wrap)

if __name__ == '__main__':
    asyncio.run(main())
