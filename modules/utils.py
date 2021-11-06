import time


def ConvertSectoDay(num):
    num = int(num)
    day = num // (24 * 3600)

    num = num % (24 * 3600)
    hour = num // 3600

    num %= 3600
    minutes = num // 60

    num %= 60
    seconds = num

    result = f'{day}d:{hour}:{minutes}:{seconds}'
    return result


def get_timezone():
    return ConvertSectoDay(time.monotonic())
