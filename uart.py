import serial
import time

ser = serial.Serial('/dev/tty.usbmodem14201', 9600, timeout=1)
ser.reset_input_buffer()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)