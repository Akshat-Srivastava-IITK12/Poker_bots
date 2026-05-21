def solve_psne(p1_matrix, p2_matrix):
  psne = []
  p1_optimum = []
  p2_optimum = []
  row = len(p1_matrix)
  col = len(p1_matrix[0])
  max_val = -10000
  for j in range(col):
    for i in range(row):
        max_val = max(max_val, p1_matrix[i][j])
    for i in range(row):
        if p1_matrix[i][j] == max_val:
            p1_optimum.append((i, j))
  for i in range(row):
    for j in range(col):
      max_val = max(max_val, p2_matrix[i][j])
    for j in range(col):
      if p2_matrix[i][j] == max_val:
        p2_optimum.append((i, j))
  for x in p1_optimum:
    if x in p2_optimum:
      psne.append(x)
  return psne


N = int(input("Enter Number of Rows: "))
M = int(input("Enter Number of Cols. : "))
p1_matrix = []
p2_matrix = []
row = []
print("Enter payoff for P1 : ")
for i in range(N):
    row = list(map(int, input().split()))
    p1_matrix.append(row)
print("Enter payoff for P2 : ")
for i in range(N):
    row = list(map(int, input().split()))
    p2_matrix.append(row)
print(solve_psne(p1_matrix, p2_matrix))
