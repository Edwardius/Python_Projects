"""
Problem J5/S2: Escape Room
Problem Description
You have to determine if it is possible to escape from a room. The room is an M-by-N grid with
each position (cell) containing a positive integer. The rows are numbered 1, 2, . . . , M and the
columns are numbered 1, 2, . . . , N. We use (r, c) to refer to the cell in row r and column c.
You start in the top-left corner at (1, 1) and exit from the bottom-right corner at (M, N). If you
are in a cell containing the value x, then you can jump to any cell (a, b) satisfying a × b = x. For
example, if you are in a cell containing a 6, you can jump to cell (2, 3).
Note that from a cell containing a 6, there are up to four cells you can jump to: (2, 3), (3, 2), (1, 6),
or (6, 1). If the room is a 5-by-6 grid, there isn’t a row 6 so only the first three jumps would be
possible.
Input Specification
The first line of the input will be an integer M (1 ≤ M ≤ 1000). The second line of the input will
be an integer N (1 ≤ N ≤ 1000). The remaining input gives the positive integers in the cells of
the room with M rows and N columns. It consists of M lines where each line contains N positive
integers, each less than or equal to 1 000 000, separated by single spaces.
For 1 of the 15 available marks, M = 2 and N = 2.
For an additional 2 of the 15 available marks, M = 1.
For an additional 4 of the 15 available marks, all of the integers in the cells will be unique.
For an additional 4 of the 15 available marks, M ≤ 200 and N ≤ 200.
Output Specification
Output yes if it is possible to escape from the room. Otherwise, output no.
Sample Input
3
4
3 10 8 14
1 11 12 12
6 2 3 9
Output for Sample Input
yes
La version franc¸aise figure a la suite de la version anglaise. `
Explanation of Output for Sample Input
Starting in the cell at (1, 1) which contains a 3, one possibility is to jump to the cell at (1, 3).
This cell contains an 8 so from it, you could jump to the cell at (2, 4). This brings you to a cell
containing 12 from which you can jump to the exit at (3, 4). Note that another way to escape is to
jump from the starting cell to the cell at (3, 1) to the cell at (2, 3) to the exit.
Notes
1. The online grader begins by testing submissions using the sample input. All other tests are
skipped if the sample test is not passed. If you are only attempting the first three subtasks
(the first 7 marks), then you might want to handle the specific values of the sample input as
a special case.
2. For the final subtask (worth 2 marks), if you are using Java, then Scanner will probably
take too long to read in the large amount of data. A much faster alternative is BufferedReader.
"""
N = int(input())
M = int(input())

Room = [[0 for u in range(N)] for u in range(M)]
Row = []
roomChecker = [[True for u in range(N)] for u in range(M)]

for i in range(N):
    Row = input().split()
    counter = 0
    for j in Row:
        Room[counter][i] = int(j)
        counter += 1

isTherePath = False
go = True

def pathFinder(coordinate, value, checker, Go):
    if Go == False:
        return()
    if checker == True:
        roomChecker[int(coordinate[0]) - 1][int(coordinate[1]) - 1] = False
    if checker == False:
        return()
    if coordinate == [M, N]:
        global isTherePath
        global go
        go = False
        isTherePath = True
        return()
    factorPairs = []
    for i in range(value + 1):
        if i == 0:
            continue
        if value % i == 0:
            corros = value/i
            pair = [i, corros]
            factorPairs.append(pair)
        else:
            continue
    for j in factorPairs:
        coordinate = j
        x = int(coordinate[0] - 1)
        y = int(coordinate[1] - 1)
        try:
            pathFinder(coordinate, Room[x][y], roomChecker[x][y], go)
        except:
            continue
    try:
        roomChecker[int(coordinate[1]) - 1][int(coordinate[0]) - 1] = True
    except:
        return()
    return()


pathFinder([1, 1], Room[0][0], roomChecker[0][0], go)
if(isTherePath == True):
    print("Yes")
else:
    print('No')