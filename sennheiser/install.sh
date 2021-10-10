#/bin/bash

rm -rf linux-*/
apt source linux
cd linux-*/
cp -v /lib/modules/`uname -r`/build/.config .
cp -v /lib/modules/`uname -r`/build/Module.symvers .
perl -pi -e "s/EXTRAVERSION =/EXTRAVERSION = `uname -r | cut -d - -f 2,3`/g" Makefile
patch -p0 < ../kernelpatch
make clean
make modules_prepare
make M=sound/usb
killall pulseaudio
sudo rmmod snd-usb-audio
sudo cp -v /lib/modules/`uname -r`/kernel/sound/usb/snd-usb-audio.ko /lib/modules/`uname -r`/kernel/sound/usb/snd-usb-audio.ko.old
sudo cp -v ./sound/usb/snd-usb-audio.ko /lib/modules/`uname -r`/kernel/sound/usb/snd-usb-audio.ko
sudo modprobe snd-usb-audio
cd ..
