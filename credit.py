from cs50 import get_int
import sys

while True:
    num = get_int("Number: ")
    if type(num) is not int:
        print("Number: foo")
    else:
        break
newNum = num
lengths = [13, 15, 16]
if len(str(newNum)) not in lengths:
    print("INVALID")
    sys.exit(0)

evenSum = 0
oddSum = 0
for i in range(len(str(newNum))):
    evenSum += newNum % 10
    newNum //= 10
    odd = 2*(newNum % 10)
    if odd > 9:
        oddSum += odd % 10
        oddSum += odd // 10
    else:
        oddSum += odd
    newNum //= 10
totalSum = oddSum + evenSum
newNum = num
if totalSum % 10 != 0:
    print("INVALID")
    sys.exit(0)
else:
    if int(str(newNum)[:1]) == 4:
        print("VISA")
    else:
        newNum = int(str(newNum)[:2])
        if newNum > 50 and newNum < 56:
            print("MASTERCARD")
        elif newNum == 34 or newNum == 37:
            print("AMEX")