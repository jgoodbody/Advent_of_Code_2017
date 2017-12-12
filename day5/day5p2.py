f = open("input5.txt","r")
for line in f:
    path.append(line[:-1])
path = [int(x) for x in path]

#part 2
def loopedList2(numberList):
    steps = 0
    i = 0
    while True:
        try:
            jump = numberList[i]
            if jump >= 3:
                numberList[i] -= 1
            else:
                numberList[i] += 1
            i += jump
            steps += 1
        except IndexError:
            return steps
			
print(loopedList2(path))