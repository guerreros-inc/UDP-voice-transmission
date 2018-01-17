#!/usr/bin/python

import socket
import pyaudio
import wave

CHUNK = 64
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 64000
WIDTH = 2

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

HOST = '0.0.0.0'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (HOST,PORT)
s.bind(server_addr)

while 1:
    data, address = s.recvfrom(8192)
    stream.write(data)
