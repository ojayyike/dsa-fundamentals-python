import bisect


word_list = 'the quick brown fox jumps over the lazy dog'
words = word_list.split(" ")
print(words)
print(sorted(words,key=str.lower))
print(sorted(words,key=len))


#Managing ordered sequences with bisect
words.sort()
print(words)
print(bisect.bisect(words,'jumps'))


#Can use bisect to perform table lookups

def grades(score,breakpoints=[60,70,80,90],grades='FDCBA'):
    i = bisect.bisect(breakpoints,score)
    return grades[i]

print([grades(score) for score in [33,67,99,77,70,89,90,100]])
