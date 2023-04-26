from machine import Pin, SoftI2C
import time

from m5_8encoder import M5_8encoder

i2c = SoftI2C(sda=Pin(2), scl=Pin(1), freq=50000)
ate_encoder = M5_8encoder(i2c)

while True:
    encoders = ate_encoder.read_all_counters()
    for enc in range(ate_encoder.ENCODERS):
        val = (encoders[enc] * 4) % 255
        ate_encoder.set_led(enc, bytes([val] * 3))

    time.sleep(0.1)
