def read_matrix(rows, cols, label):
    print(f"\nEnter {label}:")
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


# Main block

# --- Part A: Transpose ---
print("=== Part A: Transpose a Matrix ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols, "the matrix")

print("\nOriginal Matrix:")
print_matrix(matrix)

print("\nTransposed Matrix:")
print_matrix(transpose(matrix))

# --- Part B: Add Two Matrices ---
print("\n=== Part B: Add Two Matrices ===")
rows_b = int(input("Enter number of rows: "))
cols_b = int(input("Enter number of columns: "))
matrix_a = read_matrix(rows_b, cols_b, "Matrix A")
matrix_b = read_matrix(rows_b, cols_b, "Matrix B")

print("\nSum of Matrices:")
print_matrix(add_matrices(matrix_a, matrix_b))

# --- Part C: Multiply Two Matrices ---
print("\n=== Part C: Multiply Two Matrices ===")
rows_m = int(input("Enter number of rows for Matrix A: "))
cols_m = int(input("Enter number of columns for Matrix A (= rows for Matrix B): "))
cols_p = int(input("Enter number of columns for Matrix B: "))

mat_a = read_matrix(rows_m, cols_m, "Matrix A")
mat_b = read_matrix(cols_m, cols_p, "Matrix B")

print("\nProduct of Matrices (A x B):")
print_matrix(multiply_matrices(mat_a, mat_b))