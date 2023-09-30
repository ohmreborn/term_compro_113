
# Students don't submit this code to elab

# ใช้ newton methods ในการประมาณค่า square root แล้วจัดรูปนิดหน่อยเพราะคำนวณแบบนี้มันเร็วกว่าเพราะอะไรไม่รู้
# https://study.com/learn/lesson/how-to-use-newtons-method-to-find-roots-of-equations.html
def square_root(a,l=10**-6):
    x = a
    while abs(x**2 - a) >=l:
        x = (x + a/x)*0.5
    return x

"""
อีกอันจำไม่ได้ เพราะไม่ได้ทำ
"""

### Submimt your code

class Martix_multiplication_error(Exception):
    def __init__(self):
        """
        >>> try:
                raise Martix_multiplication_error
            except Exception as e:
                print(e)
            ERROR: Cannot multiply two input matrices!
        """
        self.message = "ERROR: Cannot multiply two input matrices!"
        super(Martix_multiplication_error,self).__init__(self.message)

class Matrix_subtraction_error(Exception):
    def __init__(self):
        """
        >>> try:
            raise Matrix_subtraction_error
        except Exception as e:
            print(e)
        ERROR: Cannot subtract two input matrices!
        """
        self.message = "ERROR: Cannot subtract two input matrices!"
        super(Matrix_subtraction_error,self).__init__(self.message)

class Matrix_addition_error(Exception):
    def __init__(self):
        """
        >>> try:
            raise Matrix_addition_error
        except Exception as e:
            print(e)
        ERROR: Cannot add two input matrices!
        """
        self.message = "ERROR: Cannot add two input matrices!"
        super(Matrix_addition_error,self).__init__(self.message)


class Matrix():
    def __init__(self,val):
        """
        >>> A = Matrix([[1,2,3],[4,5,6]])
        >>> A
        matrix([[1, 2, 3]
                [4, 5, 6]])
        -----------------or-------------------
        >>> a = '1 -3 4 3\n2 -5 6 6\n-3 3 4 6'
        >>> A = Matrix(a)
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> A.T
        matrix([[1, 2, -3]
                [-3, -5, 3]
                [4, 6, 4]
                [3, 6, 6]])
        -----------------and------------------
        >>> A.shape
        (3,4)
        >>> A.T.shape
        (4, 3)
        """
        if isinstance(val,str): # check is input string type?
            val = Matrix.from_string(val) # if true then convert it to a list2d
        self.val = val
        self.shape = (len(self),len(self[0]))
        self.T = self.__new__(Matrix,self)
    def __new__(cls,val):
        """
        create a new object with out use __init__ function for attribute 'self.T'
        """
        mat_tranpose = Matrix.tranpose(val)
        new_obj = super().__new__(cls)
        new_obj.val = mat_tranpose
        new_obj.shape = (len(new_obj),len(new_obj[0]))
        new_obj.T = val
        return new_obj
    @staticmethod
    def from_string(txt):
        """
        this function create for read a string fuction and convert it to a list Object.
        >>> a = '1 -3 4 3\n2 -5 6 6\n-3 3 4 6'
        >>> A = Matrix.from_string(a)
        >>> A
        [[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]]
        """
        val = []
        for row in txt.split("\n"):
            line = []
            for r in row.split():
                if "." in r:
                    line.append(float(r))
                else:
                    line.append(int(r))
            val.append(line)
        return val
    @classmethod
    def from_file(cls,filename):
        """
        read a file then convert to list from Matrix.from_string in '__init__' function
        >>> f = open('matrix_A.txt','w')
        >>> f.write('1 -3 4 3\n2 -5 6 6\n-3 3 4 6')
        26
        >>> f.close()
        >>> A = Matrix.from_file('matrix_A.txt')
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        """
        with open(filename,'r') as f:
            mat = f.read()
        return cls(mat)
    @staticmethod
    def tranpose(mat):
        """
        this function create for transpose a matrix
        >>> Matrix.tranpose(A)
        [[1, 2, -3], [-3, -5, 3], [4, 6, 4], [3, 6, 6]]
        Note. this function will return to a list object not matrix object
        """
        res = []
        for i in range(len(mat[0])):
            row = []
            for j in range(len(mat)):
                row.append(mat[j][i])
            res.append(row)
        return res

    def __len__(self):
        """
        return len of a val
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> len(A)
        3
        """
        return len(self.val)
    def __getitem__(self,index):
        """
        return element of a value in index
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> A[0]
        [1, -3, 4, 3]
        """
        return self.val[index]
    def __add__(self,other):
        """
        matrix plus a matrix
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> A + A
        matrix([[2, -6, 8, 6]
                [4, -10, 12, 12]
                [-6, 6, 8, 12]])
        >>> A + A.T
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            File "/Users/krittiwitkampradam/Downloads/python/termproject_4_v2.py", line 190, in __add__
              raise Matrix_addition_error
          Matrix_addition_error: ERROR: Cannot add two input matrices!
        """
        if self.shape != other.shape:
            raise Matrix_addition_error
        else:
            mat = []
            for a,b in zip(self.val,other.val):
                row = []
                for i,j in zip(a,b):
                    row.append(i+j)
                mat.append(row)
            return Matrix(mat)
    def __sub__(self,other):
        """
        matrix minus a matrix
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> A-A
        matrix([[0, 0, 0, 0]
                [0, 0, 0, 0]
                [0, 0, 0, 0]])
        >>> A - A.T
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            File "/Users/krittiwitkampradam/Downloads/python/termproject_4_v2.py", line 219, in __sub__
              raise Matrix_subtraction_error
          Matrix_subtraction_error: ERROR: Cannot subtract two input matrices!
        """
        if self.shape != other.shape:
            raise Matrix_subtraction_error
        else:
            mat = []
            for a,b in zip(self.val,other.val):
                row = []
                for i,j in zip(a,b):
                    row.append(i-j)
                mat.append(row)
            return Matrix(mat)
    
    def __mul__(self,other):
        """
        matrix multiplication a matrix
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> A*A.T
        matrix([[35, 59, 22]
                [59, 101, 39]
                [22, 39, 70]])
        >>>  A * 2
        matrix([[2, -6, 8, 6]
                [4, -10, 12, 12]
                [-6, 6, 8, 12]])
        >>> A * A
          Traceback (most recent call last):
            File "<stdin>", line 1, in <module>
            File "/Users/krittiwitkampradam/Downloads/python/termproject_4_v2.py", line 263, in __mul__
              raise Martix_multiplication_error
          Martix_multiplication_error: ERROR: Cannot multiply two input matrices!
        """
        
        if isinstance(other,int) or isinstance(other,float):
            res = []
            for i in range(len(self)):
                row = []
                for j in range(len(self[0])):
                    row.append(self[i][j]*other)
                res.append(row)
            return Matrix(res)
        else:
            if self.shape[1] != other.shape[0]:
                raise Martix_multiplication_error
            else:
                res = []
                for i in range(len(self)):
                    row = []
                    for j in range(len(other[0])):
                        total = 0
                        for k in range(len(self)):
                            total += self[i][k]*other[k][j]
                        row.append(total)
                    res.append(row)
                return Matrix(res)
    def __rmul__(self,other):
        """
        this function is look like __mul__ but
        this is impliment for this case
        >>> 2 * A
        matrix([[2, -6, 8, 6]
                [4, -10, 12, 12]
                [-6, 6, 8, 12]])
        """
        return self.__mul__(other)
        
    def print(self,end="\n"):
        """
        print a value of this matrix
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> A.print()
        [[1, -3, 4, 3]
         [2, -5, 6, 6]
         [-3, 3, 4, 6]]
        """
        return print(self,end=end)
    def __repr__(self):
        """
        show real value of this object in python shell
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        """
        res = "matrix([" + repr(self[0])
        for i in range(1,len(self.val)):
            res += "\n"+" "*8 + repr(self[i]) 
        res += "])"
        return res
    def __str__(self):
        """
        show real value of this object in python print function
        >>> A = Matrix([[1, -3, 4, 3], [2, -5, 6, 6], [-3, 3, 4, 6]])
        >>> A
        matrix([[1, -3, 4, 3]
                [2, -5, 6, 6]
                [-3, 3, 4, 6]])
        >>> print(A)
        [[1, -3, 4, 3]
         [2, -5, 6, 6]
         [-3, 3, 4, 6]]
        """
        res = "[" + repr(self[0])
        for i in range(1,len(self)):
            res += "\n"+" " + repr(self[i]) 
        res += "]"
        return res
    def sqrt(self):
        """
        >>> A = Matrix([[1, 3, 4, 3], [2, 5, 6, 6], [3, 3, 4, 6]])
        >>> A
        matrix([[1, 3, 4, 3]
                [2, 5, 6, 6]
                [3, 3, 4, 6]])
        >>> A.sqrt()
        matrix([[1, 1.7320508100147274, 2.0000000929222947, 1.7320508100147274]
                [1.4142135623746899, 2.236067977499978, 2.4494897427875517, 2.4494897427875517]
                [1.7320508100147274, 1.7320508100147274, 2.0000000929222947, 2.4494897427875517]])
        """
        res = []
        for i in self.val:
            row = []
            for j in i:
                r = square_root(j)
                row.append(r)
            res.append(row)
        return Matrix(res)

