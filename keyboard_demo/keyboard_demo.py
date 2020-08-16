# keyboard_demo_06.py
# Play a note using a second-order difference equation
# when the user presses a key on the keyboard.

import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second 
NUMFREQ     = 12

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 2      # Decay time (seconds)
R = 2 ** (1.0/12.0)    # 1.05946309
f0 = 440.0    # Frequency (Hz)
FLAG = 0
# f1 = f0 * R
#f2 = f1 * R
#f3 = f2 * R
#f4 = f3 * R
#f5 = f4 * R
#f6 = f5 * R
#f7 = f6 * R
#f8 = f7 * R
#f9 = f8 * R
#f10 = f9 * R
#f11 = f10 * R

f0_arr = [0] * NUMFREQ
for i in range (0, NUMFREQ):
    f0_arr[i] = f0 * R**i

# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
om1_arr = [0] * NUMFREQ
for i in range (0, NUMFREQ):
    om1_arr[i] = 2.0 * pi * f0_arr[i]/RATE

# om1 = 2.0 * pi * float(f1)/RATE

# Filter coefficients (second-order IIR)
# a = [1, -2*r*cos(om1), r**2]
# b = [r*sin(om1)]
a0 = [1, -2*r*cos(om1_arr[0]), r**2]
a1 = [1, -2*r*cos(om1_arr[1]), r**2]
a2 = [1, -2*r*cos(om1_arr[2]), r**2]
a3 = [1, -2*r*cos(om1_arr[3]), r**2]
a4 = [1, -2*r*cos(om1_arr[4]), r**2]
a5 = [1, -2*r*cos(om1_arr[5]), r**2]
a6 = [1, -2*r*cos(om1_arr[6]), r**2]
a7 = [1, -2*r*cos(om1_arr[7]), r**2]
a8 = [1, -2*r*cos(om1_arr[8]), r**2]
a9 = [1, -2*r*cos(om1_arr[9]), r**2]
a10 = [1, -2*r*cos(om1_arr[10]), r**2]
a11 = [1, -2*r*cos(om1_arr[11]), r**2]
b0 = [r*sin(om1_arr[0])]
b1 = [r*sin(om1_arr[1])]
b2 = [r*sin(om1_arr[2])]
b3 = [r*sin(om1_arr[3])]
b4 = [r*sin(om1_arr[4])]
b5 = [r*sin(om1_arr[5])]
b6 = [r*sin(om1_arr[6])]
b7 = [r*sin(om1_arr[7])]
b8 = [r*sin(om1_arr[8])]
b9 = [r*sin(om1_arr[9])]
b10 = [r*sin(om1_arr[10])]
b11 = [r*sin(om1_arr[11])]

ORDER = 2   # filter order
# states = np.zeros(ORDER)
states0 = np.zeros(ORDER)
states1 = np.zeros(ORDER)
states2 = np.zeros(ORDER)
states3 = np.zeros(ORDER)
states4 = np.zeros(ORDER)
states5 = np.zeros(ORDER)
states6 = np.zeros(ORDER)
states7 = np.zeros(ORDER)
states8 = np.zeros(ORDER)
states9 = np.zeros(ORDER)
states10 = np.zeros(ORDER)
states11 = np.zeros(ORDER)

# x = np.zeros(BLOCKLEN)
x0 = np.zeros(BLOCKLEN)
x1 = np.zeros(BLOCKLEN)
x2 = np.zeros(BLOCKLEN)
x3 = np.zeros(BLOCKLEN)
x4 = np.zeros(BLOCKLEN)
x5 = np.zeros(BLOCKLEN)
x6 = np.zeros(BLOCKLEN)
x7 = np.zeros(BLOCKLEN)
x8 = np.zeros(BLOCKLEN)
x9 = np.zeros(BLOCKLEN)
x10 = np.zeros(BLOCKLEN)
x11 = np.zeros(BLOCKLEN)

# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)
# specify low frames_per_buffer to reduce latency -> number of frames the signals are split into

CONTINUE = True
KEYPRESS = False

def my_function(event):
    global CONTINUE
    global KEYPRESS
    global FLAG
    print('You pressed ' + event.char)
    if event.char == "a":
        FLAG = 0
    if event.char == "w":
        FLAG = 1
    if event.char == "s":
        FLAG = 2
    if event.char == "e":
        FLAG = 3
    if event.char == "d":
        FLAG = 4
    if event.char == "r":
        FLAG = 5
    if event.char == "f":
        FLAG = 6
    if event.char == "t":
        FLAG = 7
    if event.char == "g":
        FLAG = 8      
    if event.char == "y":
        FLAG = 9
    if event.char == "h":
        FLAG = 10
    if event.char == "u":
        FLAG = 11                   
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    KEYPRESS = True

root = Tk.Tk()
root.bind("<Key>", my_function)

print('Press keys for sound.')
print('Press "q" to quit')

while CONTINUE:
    root.update()

    if KEYPRESS and CONTINUE:
        # Some key (not 'q') was pressed
        if FLAG == 0:
            x0[0] = 10000.0
        if FLAG == 1:
            x1[0] = 10000.0
        if FLAG == 2:
            x2[0] = 10000.0
        if FLAG == 3:
            x3[0] = 10000.0  
        if FLAG == 4:
            x4[0] = 10000.0  
        if FLAG == 5:
            x5[0] = 10000.0
        if FLAG == 6:
            x6[0] = 10000.0
        if FLAG == 7:
            x7[0] = 10000.0 
        if FLAG == 8:
            x8[0] = 10000.0 
        if FLAG == 9:
            x9[0] = 10000.0
        if FLAG == 10:
            x10[0] = 10000.0
        if FLAG == 11:
            x11[0] = 10000.0

    

    # [y, states] = signal.lfilter(b, a, x, zi = states)
    [y0, states0] = signal.lfilter(b0, a0, x0, zi = states0)
    [y1, states1] = signal.lfilter(b1, a1, x1, zi = states1)
    [y2, states2] = signal.lfilter(b2, a2, x2, zi = states2)
    [y3, states3] = signal.lfilter(b3, a3, x3, zi = states3)
    [y4, states4] = signal.lfilter(b4, a4, x4, zi = states4)
    [y5, states5] = signal.lfilter(b5, a5, x5, zi = states5)
    [y6, states6] = signal.lfilter(b6, a6, x6, zi = states6)
    [y7, states7] = signal.lfilter(b7, a7, x7, zi = states7)
    [y8, states8] = signal.lfilter(b8, a8, x8, zi = states8)
    [y9, states9] = signal.lfilter(b9, a9, x9, zi = states9)
    [y10, states10] = signal.lfilter(b10, a10, x10, zi = states10)
    [y11, states11] = signal.lfilter(b11, a11, x11, zi = states11)

    # x[0] = 0.0 
    x0[0] = 0.0
    x1[0] = 0.0
    x2[0] = 0.0
    x3[0] = 0.0
    x4[0] = 0.0
    x5[0] = 0.0
    x6[0] = 0.0
    x7[0] = 0.0
    x8[0] = 0.0
    x9[0] = 0.0
    x10[0] = 0.0
    x11[0] = 0.0

    KEYPRESS = False

    y_total = y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11
    
    y_total = np.clip(y_total.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *y_total);    # Convert to binary binary data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
