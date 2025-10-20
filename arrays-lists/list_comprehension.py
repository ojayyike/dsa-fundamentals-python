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

#GenExps save memory because it yields items one by one instead of building a stored list in memory

for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    #A list with all 6 t shirts is never produced in this example
    print(tshirt)


#Building Lists of lists
board = [['_']*3 for i in range(3)]
print(board)
board[1][2] = 'W'
print(board)

#How this board creation behaves
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
board[1][2] = 'X'
print(board)


#A List with three references to the same list is useless
weird_board = [['_']*3] *3
print(weird_board)
weird_board[1][2] = 'Y'
print(weird_board)

#The problem with weird board is that in essence it behaves like this code:
row = ['_'] * 3
board = []
for i in range(3):
    #The same row is appended 3 times to board
    board.append(row)
print(board)
board[1][2] = 'Z'
print(board)

matrix = [[0 for row in range(3)] for col in range(5)]
print(matrix)

#Practice building matrix outside of list comp
matrix = []
for col in range(5):
    new_row = []
    for row in range(3):
        new_row.append(0)
    matrix.append(new_row)
print(matrix)

