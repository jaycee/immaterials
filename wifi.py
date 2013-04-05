import time

from scan import Cell
import serial


def calc_level(cell):
    quality = cell.quality
    num,den = quality.split('/')
    true = float(num)/float(den)
    return int(round(true * 5))


def get_level():
    cells = Cell.all('wlan0')
    cell_levels = sorted([calc_level(c) for c in cells])
    return cell_levels[-1]


def main():
    #ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        lvl = get_level()
        #ser.write(lvl)
        print lvl
        time.sleep(5)

if __name__ == '__main__':
    main()
