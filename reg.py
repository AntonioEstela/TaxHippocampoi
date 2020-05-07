#!/usr/bin/python3
def TaxiRegister(taxiList):
    
    X = input("Please enter a valid TaxiId:\t")
    Y = input("Please enter the service type:\t")

    Z = [X,Y]
    print("\n{}\n".format(taxiList))
    if len(taxiList) < 79:
        taxiList.append(Z)
        print("Taxi added successfully")
    else:
        print("We don't have enought space for more taxis\n")
    print("\n{}\n".format(taxiList))
    print("")