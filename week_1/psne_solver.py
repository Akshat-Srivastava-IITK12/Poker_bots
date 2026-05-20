def solve_psne(p1_matrix, p2_matrix):
  psne = []
  row = len(p1_matrix)
  col = len(p1_matrix[0])
  p1_best = []
  p2_best = []
  for j in range(col):
    max_payoff = -10000
    for i in range(row):
      max_payoff = max(max_payoff, p1_matrix[i][j])
    for i in range(row):
      if p1_matrix[i][j] == max_payoff:
        p1_best.append((i, j))
  for i in range(row):
    max_payoff = -10000
    for j in range(col):
      max_payoff = max(max_payoff, p2_matrix[i][j])
    for j in range(col):
      if p2_matrix[i][j] == max_payoff:
        p2_best.append((i, j))
  for x in p1_best:
    if x in p2_best:
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
