

def findOnOffBulb(pep, bulb):
    #  our logic here
    bulbsStatus = []
    on = 0
    off = 0
    for i in range(0, bulb):
        bulbsStatus.append(True)

    for i in range(2, pep+1):
        tmp = i
        while True:
            if(tmp <= bulb):
                if(bulbsStatus[tmp-1]):
                    bulbsStatus[tmp-1] = False
                else:
                    bulbsStatus[tmp-1] = True
            else:
                break
            tmp *= i


    on = bulbsStatus.count(True)
    off = bulbsStatus.count(False)
    return [on, off]

if __name__ == "__main__":
    noOfPep = int(input("Enter number of people: "))
    noOfBulb = int(input("Enter number of bulbs: "))

    # find no of bulbs on or off
    result = findOnOffBulb(noOfPep, noOfBulb)

    print("no of bulbs on: ", result[0])
    print("no of bulbs off: ", result[1])
