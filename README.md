# M5 8Encoder

This is a MicroPython library for the [M5 8-Encoder](https://shop.m5stack.com/products/8-encoder-unit-stm32f030).

Features:

- ✅ Read encoder counter values
- ✅ Read encoder increment values
- ✅ Reset counter values
- ✅ Read button values
- ✅ Read switch value
- ✅ Set LEDs
- ✅ Read firmware version

## Usage

```python
from machine import Pin, SoftI2C
from m5_8encoder import M5_8Encoder

i2c = SoftI2C(sda=Pin(SDA_PIN_NUM), scl=Pin(SCL_PIN_NUM), freq=100000)
encoder = M5_8Encoder(i2c)
```

See the `examples` folder for a basic example of how to utilise the `M5_8Encoder` object, and see `m5_8encoder.py` for the class definition and all of the available methods.
You will need to ensure you're setting SDA and SCL pin numbers correctly, and note that the examples here use the `SoftI2C` module but you could also use `I2C` (hardware I2C instead of software I2C) depending on your port / board.
