import array

#Build a list of codepoints from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

#List Comprehension Verison
print([ord(symbol) for symbol in symbols])


#Cartesian product of sizes and colors using list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

#Naive Approach
for color in colors:
    for size in sizes:
        print([color,size])

#List Comp
print([(color,size) for size in sizes for color in colors])

#Generator Expresssions

#Initialize a tuple and an array from a generator expression
codes = tuple(ord(symbol) for symbol in symbols)
print(codes)
arr = array.array("I",codes)
print(arr)
