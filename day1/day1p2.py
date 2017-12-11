num = open('input1.txt','r')
input1 = int(num.readline()[:-1])

def advent1_2(n):
    digitList = [int(d) for d in str(n)]
    lengthHalf = int((len(digitList) + 1)/2)
    stringSum = 0
    for i in range(lengthHalf):
        if digitList[i] == digitList[i+lengthHalf]:
            stringSum += digitList[i]
    x = 0
    for i in range(lengthHalf,len(digitList)):
        if digitList[i] == digitList[x]:
            stringSum += digitList[i]
        x += 1
    return stringSum
	
print(advent1_2(input1))
#answer = 1393