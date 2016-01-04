import numpy as np

# first matrix stored as adjacency ordered pairs
matrix_one = [[1, 3], [1, 5], [1, 7],
              [2, 4], [2, 8], [3, 5],
              [3, 8], [4, 2], [4, 6],
              [5, 1], [5, 2], [5, 7],
              [5, 8], [6, 3], [7, 1],
              [7, 5], [7, 6], [8, 6],
              [8, 7]]

# second matrix stored as sparse matrix
matrix_two = [[0, 0, 1, 0, 0, 1, 1, 1],
              [0, 0, 1, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 1],
              [0, 1, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 1, 0, 1, 1, 0],
              [1, 0, 0, 1, 1, 0, 0, 1],
              [1, 0, 1, 1, 1, 0, 0, 0],
              [1, 0, 1, 0, 0, 1, 0, 0]]

# convert matrix one to numpy matrix to check result
matrix_one_np = np.matrix([[0, 0, 1, 0, 1, 0, 1, 0],
                           [0, 0, 0, 1, 0, 0, 0, 1],
                           [0, 0, 0, 0, 1, 0, 0, 1],
                           [0, 1, 0, 0, 0, 1, 0, 0],
                           [1, 1, 0, 0, 0, 0, 1, 1],
                           [0, 0, 1, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 1, 1, 0]])

# convert matrix two to numpy matrix to check result
matrix_two_np = np.matrix([[0, 0, 1, 0, 0, 1, 1, 1],
                           [0, 0, 1, 1, 0, 0, 0, 0],
                           [1, 1, 0, 0, 0, 0, 1, 1],
                           [0, 1, 0, 0, 1, 1, 1, 0],
                           [0, 0, 0, 1, 0, 1, 1, 0],
                           [1, 0, 0, 1, 1, 0, 0, 1],
                           [1, 0, 1, 1, 1, 0, 0, 0],
                           [1, 0, 1, 0, 0, 1, 0, 0]])

# initialize result matrix
result = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]

# initialize variables to count iterations and "multiplications"
multiplications = 0
iterations = 0

# main cross product loop.
for i in range(0, len(matrix_one)):
    for j in range(0, len(matrix_two[matrix_one[i][1] - 1])):
        iterations += 1
        if matrix_two[matrix_one[i][1] - 1][j] == 1:
            result[matrix_one[i][0] - 1][j] += 1
            multiplications += 1

# get numpy dot product
result_np = np.dot(matrix_one_np, matrix_two_np)

# print results
print "Ma Length: " + str(len(matrix_one))
print "N: 8"
print "Supposed Worst Case Multiplications: " + str(8 * len(matrix_one))
print "Multiplications: " + str(multiplications)
print "Iterations: " + str(iterations)

if np.equal(np.matrix(result), result_np).all():
    print "NumPy dot product equal to result."
else:
    print "Not Equal!"
