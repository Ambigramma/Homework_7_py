def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [[0] * num_columns for _ in range(num_rows)]
    for row in range(num_rows):
        for column in range(num_columns):
            table[row][column] = operation(row+1, column+1)
    for row in range(num_rows):
        print(" ".join(str(table[row][col]) for col in range(num_columns)))

print_operation_table(lambda x, y: x * y)
