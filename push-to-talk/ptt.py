#!/usr/bin/python3
# conf
# to get a list of valid buttons, run evtest and select your device
# to find the name of your mic, run arecord -l
# to find your microphone toggle option, run amixer -c <mic> controls
# chuck ptt.py into /usr/local/bin/
# chuck ptt.service into /etc/systemd/system/
# systemctl --enable ptt.service

PTTKey='KEY_STOP'
PTTSource='/dev/input/by-id/usb-Logitech_Gaming_Mouse_G600_342192E245030017-if01-event-kbd'
PTTMic='Microphone'
PTTMicToggle="'Mic Capture Switch'"

# no conf below here

import subprocess
from evdev import InputDevice, categorize, ecodes
dev = InputDevice(PTTSource)

for event in dev.read_loop():
    # print(categorize(event))
    if event.code == ecodes.ecodes[PTTKey]:
        match event.value:
            case 0:
                subprocess.run(['/usr/bin/amixer', '-qc', PTTMic, 'cset', 'name=' + PTTMicToggle, '0'])
            case 1:
                subprocess.run(['/usr/bin/amixer', '-qc', PTTMic, 'cset', 'name=' + PTTMicToggle, '1'])
