def printOperationTable(operation, numRows=9, numColumns=9):
  list_columns = [i+1 for i in range(0, num_columns)]
  list_rows = [i+1 for i in range(0, num_rows)]

for y in list_rows:
  new_list_row = list()

for x in list_columns:
  new_list_row.insert(x, operation)
  print(new_list_row)

printOperationTable(lambda x, y: 2*3)
