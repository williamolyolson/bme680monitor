from datetime import datetime
import board
import busio
import adafruit_bme680

#degc to degf
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
#print('Temperature: {} degrees C'.format(sensor.temperature))
#print('Gas: {} ohms'.format(sensor.gas))
#print('Humidity: {}%'.format(sensor.humidity))
#print('Pressure: {}hPa'.format(sensor.pressure))
outputfile = '/var/www/html/index.html'
outfile = open(outputfile,'w')
outfile.write('<html><head></head><body>')
outfile.write('<table><tr><th>Humidity(%)</th><td>{}</td>' .format(round(sensor.humidity,2)))
outfile.write('<th>Temperature(F)</th><td>{}</td></tr>'.format(round(c_to_f(sensor.temperature),2)))
outfile.write('<tr><th>Gas(ohms)</th><td>{}</td>'.format(sensor.gas))
outfile.write('<th>Pressure(hpa)</th><td>{}</td></tr>'.format(round(sensor.pressure,2)))
outfile.write('<tr><th>Time Stamp</th><td>{}</td></tr>'.format(datetime.now(tz=None)))
outfile.write('</table></body></html>')
outfile.close();

