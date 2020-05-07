#!/usr/bin/python3
import simplytaxi
import premiumtaxi
import reg
from taxilist import taxiList

print("\nWelcome to the new system of Tax Hippokampoi")
print("Terminal: Buenavista #2 Shopping Mall\n\n")
while True:
    if len(taxiList) <= 10:
        print("Please request more Taxis to this location\n")
    print("Please entry one of the following options:\n")
    X = input("1 - TaxiX -- New simply Taxi order -- \n2 - TaxiGold -- New premium Taxi order --\n3 - Register new vehicle\n4 - Exit\n\nOption: ")
    X = int(X)
    print("")
    if X == 1:
        simplytaxi.TaxiX(taxiList)

    elif X == 2:
        premiumtaxi.TaxiGold(taxiList)

    elif X == 3:
        reg.TaxiRegister(taxiList)

    elif X == 4:
        break
    else:
        print("Please enter valid option\n")
