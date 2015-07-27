#! /usr/bin/python3
import os
import RPi.GPIO as G
from time import sleep

# Monta o pendrive apartir da ultima linha do arquivo /etc/fstab
os.system('sudo mount -a')

G.setmode(G.BOARD)

# Set relay pins as output
G.setup(7, G.OUT)

sleep(1)

achou = False

for root, dirs, files in os.walk('/media/usb'):
	for musica in files:
		isMusica = musica.lower()
		if isMusica.endswith('.mp3'):
			achou = True


if achou:
	os.system('mpg123 /media/usb/*.mp3')
else:
	os.system('mpg123 Toque.mp3')

os.system('sudo umount /media/usb')

sleep(1)
G.setup(7, G.HIGH)