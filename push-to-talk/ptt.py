#!/usr/bin/python3
# you must have read permission on the /dev/input device to be able to do this
# this is probably a really bad idea on a keyboard
# conf
PTTKey='F20'
PTTSource='/dev/input/by-id/usb-Logitech_Gaming_Mouse_G600_342192E245030017-if01-event-kbd'
PTTMic='alsa_input.usb-Antlion_Audio_Antlion_Wireless_Microphone-00.mono-fallback'
# no conf below here

import subprocess
from evdev import InputDevice, categorize, ecodes
dev = InputDevice(PTTSource)

for event in dev.read_loop():
    if event.code == ecodes.ecodes['KEY_'+PTTKey]:
        match event.value:
            case 0:
                subprocess.run(['/usr/bin/pactl', 'set-source-mute', PTTMic, '1'])
            case 1:
                subprocess.run(['/usr/bin/pactl', 'set-source-mute', PTTMic, '0'])
