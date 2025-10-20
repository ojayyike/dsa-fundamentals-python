def find_smallest(arr):
    idx = 0
    smallest = arr[idx]

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            idx = i
    return idx

def selection_sort(arr):
    new_list = []
    copy = list(arr)
    for i in range(len(arr)):
        smallest = find_smallest(copy)
        new_list.append(copy.pop(smallest))
    return new_list

print(selection_sort([5,7,3,4,1]))
