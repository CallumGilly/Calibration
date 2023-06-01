import Calibration


def calibrate():
    altitude = int(input("Enter altitude: "))
    needed_altitudes = Calibration.get_alts_needed(altitude)
    adj1 = int(input("Adj at " + str(needed_altitudes[0]) + "ft: "))
    adj2 = int(input("Adj at " + str(needed_altitudes[1]) + "ft: "))

    print(str(Calibration.calibrate(altitude, needed_altitudes, [adj1, adj2])) + "ft")


while True:
    print("\n====================")
    print("1) Calibration")
    try:
        option = int(input("Select prog: "))
        if option == 1:
            calibrate()
    except ValueError:
        print("Invalid input");
        pass



