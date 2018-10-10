import random
import numpy
table_matrix =  [[],[],[]citrix
]
def gen_table_no():
  return random.randint(0,2)

while(True):
  name = input("Enter your name: ")
  not_assigned = True
  while(not_assigned):
    selected_table = gen_table_no()
    if len(table_matrix[selected_table]) < 3:
      print("DEBUG:check which table is selected : {}".format(selected_table))
      table_matrix[selected_table].append(name)
      print(table_matrix)
      not_assigned == False
      print("{} San, Your table is {}".format(name, selected_table))
    else:
      print("The table {} is full, let's find again :".format(selected_table))
    break

  for table in table_matrix:
    print(*table)