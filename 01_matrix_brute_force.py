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
    :time complexity: O((r*c)^2) r being the number of rows and c being the number of columns
    """
    # compute the sizes
    numberOfRows = len(matrix)
    numberOfColumns = len(matrix[0])
    # construct the output matrix
    outPutMatrix = [[0] * numberOfColumns for i in range(numberOfRows)]
    # loop to fill in the matrix
    for row in range(numberOfRows):
        for column in range(numberOfColumns):
            if matrix[row][column] == 0:
                outPutMatrix[row][column] = 0
            else:
                minDistance = max(numberOfRows, numberOfColumns) + 1
                for i in range(numberOfRows):
                    for j in range(numberOfColumns):
                        if matrix[i][j] == 0 and (i != row or j != column):
                            distance = abs(i - row) + abs(j - column)
                            if distance < minDistance:
                                minDistance = distance
                outPutMatrix[row][column] = minDistance
    return outPutMatrix

# A = [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# print(updateMatrix(A))
#
# B= [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# print(updateMatrix(B))
