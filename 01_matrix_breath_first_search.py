# author: YANG CUI
"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]
Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

Brute Force Approach
"""

def updateMatrix(matrix):
    """
    :param matrix: input matrix containing only 0s and 1s.
    :return: output matrix containing the minimal distances.
    :time complexity: O(r * c) r being the number of rows and c being the number of columns
    """
    # compute the sizes
    numberOfRows = len(matrix)
    numberOfColumns = len(matrix[0])
    # construct the output matrix
    outPutMatrix = [[0] * numberOfColumns for i in range(numberOfRows)]
    # construct the queue
    queueOfZeros = []
    # one pass to initialize the matrix as well as push all the 0 cells in the queue
    for row in range(numberOfRows):
        for column in range(numberOfColumns):
            if matrix[row][column] == 0:
                outPutMatrix[row][column] = 0
                queueOfZeros.append([row,column])
            else:
                outPutMatrix[row][column] = numberOfRows + numberOfColumns
    # directions
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # second pass to fill in the result matrix
    while len(queueOfZeros) != 0:
        current = queueOfZeros.pop()
        for i in range(len(directions)):
            new_row = current[0] + directions[i][0]
            new_col = current[1] + directions[i][1]
            if (new_row >= 0 and new_col >= 0 and new_row < numberOfRows and new_col < numberOfColumns):
                if outPutMatrix[new_row][new_col] > outPutMatrix[current[0]][current[1]] + 1:
                    outPutMatrix[new_row][new_col] = outPutMatrix[current[0]][current[1]] + 1
                    queueOfZeros.append([new_row, new_col])

    return outPutMatrix

# A = [[0,0,0],
# #  [0,1,0],
# #  [0,0,0]]
# # print(updateMatrix(A))

# B= [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# print(updateMatrix(B))
