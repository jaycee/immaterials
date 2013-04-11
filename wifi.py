import time

from scan import Cell
import serial


def convert_dbm(val):
    return (float(10)**(0.1*(val-30)))*10e11


def calc_level(cell):   
    val = int(cell.signal)
    val = float(100 + val)/10
    return int(round(val))


def get_level():
    cells = Cell.all('wlan1')
    for c in cells:
        c.level = calc_level(c)
    cells.sort(key=lambda x: x.level) 
    c = cells[-1]
    print c.ssid, c.signal, c.level
    return str(c.level)


def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    import random
    while True:
        lvl = get_level()
        ser.write(lvl)
        time.sleep(5)

if __name__ == '__main__':
    main()
