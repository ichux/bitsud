import calendar
import math
import time


def happened_at():
    present_epoch = math.floor(time.time() * 1000)
    time_at = time.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    epoch_2020 = calendar.timegm(time_at) * 1000
    return present_epoch - epoch_2020


def shift(by=10):
    return happened_at() << by


def adds(lhs, rhs):
    return lhs | rhs


def modulo(lhs, rhs):
    return lhs % rhs


if __name__ == '__main__':
    print(adds(shift(1), 0))
