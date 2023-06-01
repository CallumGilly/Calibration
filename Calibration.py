# File used to perform linear interpolation for linear interpolation charts.
import math


def get_alts_needed(alt):
    return [math.floor(alt / 1000) * 1000, math.ceil(alt / 1000) * 1000]


def calibrate(alt, needed_altitudes, adjustments):
    correction = [needed_altitudes[0] + adjustments[0],
                  needed_altitudes[1] + adjustments[1]]

    return correction[0] + (alt - needed_altitudes[0]) * (correction[1] - correction[0]) / (
            needed_altitudes[1] - needed_altitudes[0])
