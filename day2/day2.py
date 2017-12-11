# yeah i'm using pandas
# too much data analysis
import pandas as pd

data = pd.read_csv('input2.tsv',sep='\t',header=None)

#part 1
def minmax(row):
    return max(row)-min(row)
diffs = data.apply(minmax, axis=1)
print(sum(diffs))

#part 2
def modulocheck(row):
    for i in range(len(row)):
        for j in range(len(row)):
            if (row[i] % row[j] == 0) & (i != j):
                return row[i]/row[j]
            elif (row[j] % row[i] == 0) & (i != j):
                return row[j]/row[i]
				
modulos = data.apply(modulocheck,axis=1)
print(sum(modulos))