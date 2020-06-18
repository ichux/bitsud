import calendar
import math
import time


def happened_at():
    present_epoch = math.floor(time.time() * 1000)
    time_at = time.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    epoch_2020 = calendar.timegm(time_at) * 1000
    return present_epoch, epoch_2020, present_epoch - epoch_2020


def binary_operations(starts, operator, by, section="b"):
    solution = None
    operator = operator if operator in ['<<', '|', ">>"] else None

    if operator is None:
        raise ValueError(f'Unknown operator type: {operator}')

    if operator == "|":
        solution = starts | by
    if operator == "<<":
        solution = starts << by
    if operator == ">>":
        solution = starts >> by

    if solution is None:
        return None

    starts_binary = bin(starts).replace('0b', '')
    solution_binary = bin(solution).replace('0b', '')

    top = f"{starts: >20} = {starts_binary: >64} - length={len(starts_binary)}"
    down = f"{solution: > 20} = {solution_binary: >64} - length={len(solution_binary)}"

    if section == 'b':
        return f"{top}\n{down}\n"
    if section == 't':
        return top
    if section == 'd':
        return down


if __name__ == '__main__':
    # print(binary_operations(1387263000, "<<", 23, 'd'))
    # print(binary_operations(1023, "<<", 10, 'd'))
    # print(binary_operations(11637205499904000, "|", 1047552, 'd'))

    # a, b, difference = happened_at()
    difference = 14554375468
    print(binary_operations(difference, "<<", 10))
    print(binary_operations(14903680479232, "|", 5))
