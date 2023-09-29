def readMat(fn):
  m = []
  with open(fn) as fp:
    for line in fp:
      m.append(line.strip().split(' '))
  return m

def printMat(m):
  for i in range(len(m)):
    row = ''
    for j in range(len(m[0])):
      row += f'{m[i][j]:^8}'
    print(row)
  print()
