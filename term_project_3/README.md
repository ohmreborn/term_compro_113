จงแก้สมการ จาก[ไฟล์ที่แนบมา](https://github.com/ohmreborn/term_compro_113/tree/main/term_project_3/test)ให้โดยใช้ gaussian elimination
## case 1
```
Enter filename: test/gauss01.txt
Augmented matrix:
   1       -3      4       3    
   2       -5      6       6    
   -3      3       4       6    

R1->R1/(1) [1, -3, 4, 3]
R2->R2/(2) [1, -5/2, 3, 3]
R2 ==> R2 - R1
   1       -3      4       3    
   0      1/2      -1      0    
   -3      3       4       6    

R3->R3/(-3) [1, -1, -4/3, -2]
R3 ==> R3 - R1
   1       -3      4       3    
   0      1/2      -1      0    
   0       2     -16/3     -5   

R2->R2/(1/2) [0, 1, -2, 0]
R3->R3/(2) [0, 1, -8/3, -5/2]
R3 ==> R3 - R2
   1       -3      4       3    
   0      1/2      -1      0    
   0       0      -2/3    -5/2  

R2 ==> R2 / (1/2)
R3 ==> R3 / (-2/3)
   1       -3      4       3    
   0       1       -2      0    
   0       0       1      15/4  

Result from Gaussian Elimination:
   1       -3      4       3    
   0       1       -2      0    
   0       0       1      15/4  

After Back-Substitution:
a = 21/2
b = 15/2
c = 15/4
```
## case2
```
Enter filename: test/gauss02.txt
Augmented matrix:
   1       -2      3       9    
   -1      3       0       -4   
   2       -5      5       17   

R1->R1/(1) [1, -2, 3, 9]
R2->R2/(-1) [1, -3, 0, 4]
R2 ==> R2 - R1
   1       -2      3       9    
   0       -1      -3      -5   
   2       -5      5       17   

R3->R3/(2) [1, -5/2, 5/2, 17/2]
R3 ==> R3 - R1
   1       -2      3       9    
   0       -1      -3      -5   
   0      -1/2    -1/2    -1/2  

R2->R2/(-1) [0, 1, 3, 5]
R3->R3/(-1/2) [0, 1, 1, 1]
R3 ==> R3 - R2
   1       -2      3       9    
   0       -1      -3      -5   
   0       0       -2      -4   

R2 ==> R2 / (-1)
R3 ==> R3 / (-2)
   1       -2      3       9    
   0       1       3       5    
   0       0       1       2    

Result from Gaussian Elimination:
   1       -2      3       9    
   0       1       3       5    
   0       0       1       2    

After Back-Substitution:
a = 1
b = -1
c = 2
```
#
สามารถ ดู case เพิ่มเติมได้[ที่นี่](https://github.com/ohmreborn/term_compro_113/tree/main/term_project_3/testcase) และโปรดอย่าพึ่งดูเฉลย


```python
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
```
```python
### submit your code
```
