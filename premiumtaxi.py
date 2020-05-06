#!/usr/bin/python3
def TaxiGold(taxiList):
    print("\n{}\n".format(taxiList))
    for cmp in taxiList:
        if cmp[1] == 'Gold':
            print("Your TaxiGold with ID {} is incoming".format(cmp[0]))
            taxiList.remove(cmp)
            break
    else:
        print("We don't have the requested service\n")
    print("\n{}\n".format(taxiList))
    print("")