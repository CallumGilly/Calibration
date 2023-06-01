import Calibration

while True:
    try:
        print("1) Calibration")
        option = int(input("Select prog: "))
        if option == 1:
            Calibration.calibrate()
    except ValueError:
        print("Invalid input");
        pass

