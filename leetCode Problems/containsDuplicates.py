import collections
def containsDuplications(nums):
    table = collections.defaultdict(int)

    for num in nums:
        if num in table:
            return True
        table[num] = 1
    return False
