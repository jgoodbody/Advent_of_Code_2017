num = open('input1.txt','r')
input1 = int(num.readline()[:-1])

def advent1(n):
    digitList = [int(d) for d in str(n)]
    stringSum = 0
    for i in range(len(digitList)-1):
        if digitList[i] == digitList[i+1]:
            stringSum += digitList[i]
    if digitList[len(digitList)-1] == digitList[0]:
        stringSum += digitList[0]
    return stringSum

print(advent1(input1))
