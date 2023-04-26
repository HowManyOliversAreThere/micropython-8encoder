# M5 8Encoder

This is a MicroPython library for the [M5 8-Encoder](https://shop.m5stack.com/products/8-encoder-unit-stm32f030).

## Usage

```python
from machine import Pin, SoftI2C
from m5_8encoder import M5_8encoder

i2c = SoftI2C(sda=Pin(SDA_PIN_NUM), scl=Pin(SCL_PIN_NUM), freq=50000)
m5_8encoder = M5_8encoder(i2c)
```

See `test.py` for an example of how to utilise the class in a practical way, or `m5_8encoder.py` for the class definition and available methods.
