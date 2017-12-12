#i shouldn't be using pandas here
import pandas as pd

data6 = pd.read_csv('input6.txt',sep='\t',header=None)
data6 = data6.transpose().iloc[:,0]
data6 = [i for i in data6]

#part 1
def advent6(day6):
    listofLists = []
    steps = 0
    while True:
        blocks = max(day6)
        i = day6.index((max(day6)))
        j = i
        for num in range(blocks):
            day6[i] -= 1
            if j == len(day6)-1:
                j = 0
            else:
                j += 1
            day6[j] += 1
        steps += 1
        listofLists.append(list(day6))
        for i in range(len(listofLists)-1):
            if (day6==listofLists[i]) & (steps > 1): 
                break
        else:
            continue
        break
    return steps
	
print(advent6(data6))

#have to reset the list by re-reading the input
data6 = pd.read_csv('input6.txt',sep='\t',header=None)
data6 = data6.transpose().iloc[:,0]
data6 = [i for i in data6]

#part 2 (exactly the same except for returned value)
def advent6_2(day6):
    listofLists = []
    steps = 0
    while True:
        blocks = max(day6)
        i = day6.index((max(day6)))
        j = i
        for num in range(blocks):
            day6[i] -= 1
            if j == len(day6)-1:
                j = 0
            else:
                j += 1
            day6[j] += 1
        steps += 1
        listofLists.append(list(day6))
        for i in range(len(listofLists)-1):
            if (day6==listofLists[i]) & (steps > 1): 
                break
        else:
            continue
        break
    return ((steps-1) - listofLists.index(list(listofLists[len(listofLists)-1])))
	
print(advent6_2(data6))