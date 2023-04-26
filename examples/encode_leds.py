from machine import Pin, SoftI2C
import time

from m5_8encoder import M5_8Encoder

i2c = SoftI2C(sda=Pin(2), scl=Pin(1), freq=50000)
encoder = M5_8Encoder(i2c)

while True:
    encoders = encoder.read_all_counters()
    for enc in range(encoder.ENCODERS):
        val = (encoders[enc] * 4) % 255
        encoder.set_led(enc, bytes([val] * 3))

    time.sleep(0.1)
