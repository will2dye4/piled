#!/usr/bin/env python3

import time

from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219


COLUMN_DAY = 2
COLUMN_HOUR = 5
COLUMN_MINUTE = 6
COLUMN_MONTH = 1
COLUMN_SECOND = 7
COLUMN_YEAR = 0
COLUMNS = [COLUMN_YEAR, COLUMN_MONTH, COLUMN_DAY, COLUMN_HOUR, COLUMN_MINUTE, COLUMN_SECOND]
REFRESH_INTERVAL_SECONDS = 1
YEAR_OFFSET = 2000


def binary_clock(device):
    while True:
        now = datetime.now()
        fields = [now.year - YEAR_OFFSET, now.month, now.day, now.hour, now.minute, now.second]
        points = []
        for i, value in zip(COLUMNS, fields):
            for j in range(device.height):
                mask = 2 ** j
                if value & mask:
                    points.append((i, device.height - 1 - j))
        with canvas(device) as draw:
            draw.point(points, fill='white')
        time.sleep(REFRESH_INTERVAL_SECONDS)


if __name__ == '__main__':
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=2)
    binary_clock(device)
