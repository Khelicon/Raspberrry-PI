
# SHT30 I2C Temperature and Humidity

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# SHT30 address, 0x44(68), or 0x45
# Send measurement command,{0x2c, [0x06]} High repeatability measurement

bus.write_i2c_block_data(0x45, 0x2C, [0x06])

#wait
time.sleep(0.5)

# SHT30 address, 0x45
# Read 6 bytes of data back from 0x00(00)
# cTemp MSB,LSB,CRC, Humidity MSB,LSB,CRC
data = bus.read_i2c_block_data(0x45, 0x00, 6)

# Convert the data
cTemp = ((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45
fTemp = cTemp * 1.8 + 32
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Output data to screen
print "Relative Humidity : %.2f %%RH" %humidity
print "Temperature in Celsius : %.2f C" %cTemp
print "Temperature in Fahrenheit : %.2f F" %fTemp