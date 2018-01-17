#!/usr/bin/python

import socket
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 64000

HOST = '192.168.1.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (HOST,PORT)

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

while 1:
    data  = stream.read(CHUNK)
    s.sendto(data,server_addr)
