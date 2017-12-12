# more pandas
import pandas as pd

data = pd.read_csv('input4.tsv',sep='\t',header=None)

#part 1
words = data[0].str.split()
wordSets = [(len(row) == len(set(row))) for row in words]
print(sum(wordSets))

#part 2
def anagrams(x):
    anagrammed = [''.join(sorted(word)) for word in x]
    return (len(anagrammed) == len(set(anagrammed)))
wordAnagrams = words.apply(anagrams)
print(sum(wordAnagrams))