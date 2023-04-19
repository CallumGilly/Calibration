# File used to perform linear interpolation for linear interpolation charts.
import math


def get_alts_needed(alt):
    return [math.floor(alt / 1000) * 1000, math.ceil(alt / 1000) * 1000]


def calibrate(alt, needed_altitudes, adjustments):
    correction = [needed_altitudes[0] + adjustments[0],
                  needed_altitudes[1] + adjustments[1]]

    return correction[0] + (alt - needed_altitudes[0]) * (correction[1] - correction[0]) / (
            needed_altitudes[1] - needed_altitudes[0])


if __name__ == "__main__":
    while True:
        altitude = int(input("Enter the given altitude: "))
        neededAltitudes = get_alts_needed(altitude)
        adj1 = int(input("Enter the adjustment at " + str(neededAltitudes[0]) + "ft: "))
        adj2 = int(input("Enter the adjustment at " + str(neededAltitudes[1]) + "ft: "))

        print(str(calibrate(altitude, neededAltitudes, [adj1, adj2])) + "ft")
