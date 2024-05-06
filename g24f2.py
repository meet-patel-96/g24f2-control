#!/usr/bin/python3

import usb.core
import usb.util
import sys
import time

VID = 0x2109
PID = 0x8883

dev = usb.core.find(idVendor=VID, idProduct=PID)

if dev is None:
    raise IOError('Device not found')

assert len(sys.argv) >= 3, "Provide two arguments, namely brightness and contrast values."

_set_brightness = sys.argv[1]
_set_contrast = sys.argv[2]

def check_param(brightness, contrast):
    if (not brightness.isdigit() or not contrast.isdigit()) or \
        (not 0 <= int(brightness) <= 100 or not 0 <= int(contrast) <= 100):
        raise ValueError("Brigtness/contrast must be an int in range [0, 100].")

HEADER = [0x6e, 0x51, 0x84, 0x03]
MODE_BRIGHTNESS = [0x10, 0x00]
MODE_CONTRAST = [0x12, 0x00]

def set_brightness(brightness):
    data = HEADER + MODE_BRIGHTNESS + [brightness]
    dev.ctrl_transfer(0x40, 178, 0, 0, data)
    time.sleep(0.2)

def set_contrast(contrast):
    data = HEADER + MODE_CONTRAST + [contrast]
    dev.ctrl_transfer(0x40, 178, 0, 0, data)
    time.sleep(0.2)

check_param(_set_brightness, _set_contrast)

_set_brightness = int(_set_brightness)
_set_contrast =int(_set_contrast)

set_brightness(_set_brightness)
set_contrast(_set_contrast)

