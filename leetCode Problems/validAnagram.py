import collections

def validAnagram(s,t):
    freq_s = collections.Counter(s)
    freq_t = collections.Counter(t)

    return freq_s == freq_t


print(validAnagram("racecar","raceecar"))
