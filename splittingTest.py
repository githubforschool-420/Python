largeNumber = str(input("Give a large number: "))

numberInList = largeNumber.split('0', 1)
if largeNumber[0] == '0':
    numberInList.pop(0)

print(int(numberInList))
