# SPDX-FileCopyrightText: Copyright (c) 2019-2021 Gaston Williams
#
# SPDX-License-Identifier: MIT

#  This is example is for the SparkFun Qwiic Joystick.
#  SparkFun sells these at its website: www.sparkfun.com
#  Do you like this library? Help support SparkFun. Buy a board!
#  https://www.sparkfun.com/products/15168

"""
 Qwiic Joystick Simple Test - qwiicjoystick_simpletest.py
 Written by Gaston Williams, June 13th, 2019
 The Qwiic Joystick is a I2C controlled analog joystick

 Simple Test:
 This program uses the Qwiic Joystick CircuitPython Library to read
 and print out the joystick position.
"""
import sys
from time import sleep
import time
import board
import sparkfun_qwiicjoystick
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


# Create bus object using our board's I2C port
i2c = board.I2C()

# Create joystick object
joystick = sparkfun_qwiicjoystick.Sparkfun_QwiicJoystick(i2c)

# Check if connected
if joystick.connected:
    print("Joystick connected.")
else:
    print("Joystick does not appear to be connected. Please check wiring.")
    sys.exit()

print("Press Joystick button to exit program.")

# joystick.button goes to 0 when pressed

running = False
# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

N = 0 #north
S = 0 #south
W = 0 #west
E = 0 #east

while True:
    if joystick.horizontal > 514:
        N = round((joystick.horizontal - 514)/128)
        S = 0
    else:
        N = 0
        S = round((514 - joystick.horizontal)/128)
    if joystick.vertical > 514:
        E = round((joystick.vertical - 514)/128)
        W = 0
    else:
        E = 0
        W = round((514 - joystick.vertical)/128)
    if N > 0:
        print("NORTH: " + str(N))
        keyboard_layout.write(chr(ord('A') + N - 1))
    if S > 0:
        print("SOUTH: " + str(S))
        keyboard_layout.write(chr(ord('a') + S - 1))
    if E > 0:
        print("EAST: " + str(E))
        keyboard_layout.write(chr(ord('m') + E - 1))
    if W > 0:
        print("WEST: " + str(W))
        keyboard_layout.write(chr(ord('M') + W - 1))
    if joystick.button == 0:
        keyboard_layout.write(' ')
    sleep(0.010)  # sleep a bit to slow down messages

#     D
#     C
#     B
#     A
# PONM mnop
#     a
#     b
#     c
#     d
#
