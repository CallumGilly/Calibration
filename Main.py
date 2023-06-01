import Calibration
import Base36


def calibrate():
    altitude = int(input("Enter altitude: "))
    needed_altitudes = Calibration.get_alts_needed(altitude)
    adj1 = int(input("Adj at " + str(needed_altitudes[0]) + "ft: "))
    adj2 = int(input("Adj at " + str(needed_altitudes[1]) + "ft: "))

    print(str(altitude) + "ft -> " + str(Calibration.calibrate(altitude, needed_altitudes, [adj1, adj2])) + "ft")


def b10tob36():
    print("B36 Num: " + Base36.b10tob36(input("B10 Num: ")))


def b36tob10():
    print("B10 Num: " + Base36.b36tob10(input("B36 Num: ")))


while True:
    print("\n====================")
    print("1) Calibration")
    print("2) B10 -> B36")
    print("3) B36 -> B10")
    try:
        option = int(input("Select prog: "))
        if option == 1:
            calibrate()
        elif option == 2:
            b10tob36()
        elif option == 3:
            b36tob10()

    except ValueError:
        print("Invalid input");
        pass



