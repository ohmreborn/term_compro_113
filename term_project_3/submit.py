class Fraction():
    def __init__(self,num,denum=1):
        self.num = int(num)
        self.denum = int(denum)
        if self.num != 0:
            if self.denum <0:
                self.num *= -1
                self.denum *= -1

            gcd = Fraction.euclid_gcd(abs(self.num),self.denum)
            self.num //= gcd
            self.denum //= gcd
        else:
            self.denum = 1
    def __float__(self):
        """
        convert a fraction to a actual decimal number
        >>> a  = Fraction(6,27)
        >>> float(a)
        0.2222222222222222
        """
        return self.num/self.denum
    def __add__(self,cls):
        """
        Fraction plus Fraction
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
        >>> a+b
        8/9
        """
        c = Fraction.lcm(self.denum,cls.denum)
        a = (self.num * c//self.denum) + (cls.num * c//cls.denum)
        return Fraction(a,c)
    def __radd__(self,cls):
        """
        Fraction plus Fraction but I write this function for a sum function
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
        >>> a+b
        8/9
        """
        if isinstance(cls,int):
            cls = Fraction(cls)
        return self.__add__(cls)
    def __iadd__(self,cls):
        """
        Fraction += Fraction or a integers 
        ex.
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>>> a += 1
        11/9
        """
        if isinstance(cls,int):
            cls = Fraction(cls)
        return self.__add__(cls)
    def __sub__(self,cls):
        """
        Fraction minus Fraction
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
       >>> a-b
        -4/9
        """
        c = Fraction.lcm(self.denum,cls.denum)
        a = (self.num * c//self.denum) - (cls.num * c//cls.denum)
        return Fraction(a,c)
    def __mul__(self,cls):
        """
        Fraction multiplication Fraction
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
       >>> a*b
        4/27
        """
        a = self.num * cls.num
        if a == 0:
            return Fraction(a)
        else:
            b = self.denum * cls.denum
            return Fraction(a,b)
    def __truediv__(self,cls):
        """
        Fraction devide Fraction
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
       >>> a/b
        1/3
        """
        a = self.num * cls.denum
        if a == 0:
            return Fraction(a)
        else:
            b = self.denum * cls.num
            return Fraction(a,b)
    @staticmethod
    def euclid_gcd(a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a > b:
            a,b = b,a
        return Fraction.euclid_gcd(b%a,a)
    @staticmethod
    def lcm(a,b):
        return (a*b)//Fraction.euclid_gcd(a,b)

    def __eq__(self,cls):
        """
        show a value of it self
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
        >>> a == b
        False
        >>> a == a
        True
        """
        if isinstance(cls,int):
            return float(self) == cls
        else:
            return (self.num == cls.num) and (self.denum == self.denum)
        
    def __ne__(self,cls):
        """
        show a value of it self
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        >>> b = Fraction(4,6)
        >>> b
        2/3
        >>> a != b
        True
        >>> a != a
        False
        """
        if isinstance(cls,int):
            return float(self) != cls
        else:
            return (self.num != cls.num) or (self.denum != self.denum)
        
    def __repr__(self):
        """
        show a value of it self
        >>> a  = Fraction(6,27)
        >>> a
        2/9
        """
        if self.denum == 1 or self.num == 0:
            return f"{self.num}"
        else:
            return f"{self.num}/{self.denum}"

    def __format__(self,format_spec):
        """
        format a string
        >>> a  = Fraction(6,27)
        >>> f"a = {a}"
        'a = 2/9'
        >>> f"a = {a:^8}"
        'a =   2/9   '
        """
        return str.__format__(self.__repr__(),format_spec)



class vector():
    def __init__(self,val):
        """
        vector is look like a list to store a Fraction number
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        """
        self.val = []
        for v in val:
            if isinstance(v,Fraction):
                self.val.append(v)
            elif isinstance(v,int) or isinstance(v,str):
                self.val.append(Fraction(v))
            else:
                raise "value in vector should be a integer or a fraction"
            
    def sum(self):
        """
        to sum a vector
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> v.sum()
        6
        """
        if self.val == []:
            return Fraction(0)
        else:
            return sum(self.val)
    def append(self,new_val):
        """
        add new value
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> v.append(2)
        >>> v
        [1, 2, 3, 2]
        """
        if isinstance(new_val,int):
            new_val = Fraction(new_val)
        self.val.append(new_val)

    def __add__(self,cls):
        """
        plus a vector between vector
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> u = vector([8,6,2])
        >>> u
        [8, 6, 2]
        >>> u+v
        [9, 8, 5]
        """
        return vector([a+b for a,b in zip(self.val,cls.val)])

    def __sub__(self,cls):
        """
        minus a vector between vector
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> u = vector([8,6,2])
        >>> u
        [8, 6, 2]
        >>> u-v
        [7, 4, -1]
        """
        return vector([a-b for a,b in zip(self.val,cls.val)])


    def __mul__(self,cls):
        """
        multiplication a vector between vector
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> u = vector([8,6,2])
        >>> u
        [8, 6, 2]
        >>> u*v
        [8, 12, 6]
        """
        if isinstance(cls,int):
            cls = Fraction(cls)
            res = [cls*i for i in self.val]
        elif isinstance(cls,Fraction):
            res = [i*cls for i in self.val]
        else:
            res = [a*b for a,b in zip(self.val,cls.val)]
        return vector(res)
    def __truediv__(self,cls):
        """
        multiplication a vector between vector
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> u = vector([8,6,2])
        >>> u
        [8, 6, 2]
        >>> u/v
        [8, 3, 2/3]
        """
        if isinstance(cls,int):
            cls = Fraction(cls)
            res = [i/cls for i in self.val]
        elif isinstance(cls,Fraction):
            res = [i/cls for i in self.val]
        else:
            res = [a/b for a,b in zip(self.val,cls.val)]
        return vector(res)
    
    def __getitem__(self,i):
        """
        return value of element of a element
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> v[0]
        1
        """
        return self.val[i]
    def __setitem__(self,key,value):
        """
        setitem of element of vector
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> v[0] = 9
        >>> v
        [9, 2, 3]
        """
        self.val[key] = value
    def __len__(self):
        """
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        >>> len(v)
        3
        """
        return len(self.val)
    def __repr__(self):
        """
        show a value of it self
        >>> v = vector([1,2,3])
        >>> v
        [1, 2, 3]
        """
        return repr(self.val)
  
class matrix(vector):
    """
    this matrix class is a 2d vector
    """
    def __init__(self,val):
        self.val = vector([])
        for i in val:
            self.val.append(vector(i))
    def switch(self,row1,row2):
        """
        switch elemtnt in metrix
        """
        a = self.val[row1]
        b = self.val[row2]
        self.val[row1] = b
        self.val[row2] = a

# ---------------------gaussian elimination-------------------------------

filename = input("Enter filename: ")
m = readMat(filename)
m = matrix(m)

print("Augmented matrix:")
printMat(m)
def switch(show):
    global m
    if float(m[col][col]) == 0:
        ind = col
        while float(m[ind][ind]) == 0:
            ind += 1
        if show:
            print(f"R{col+1}<=>R{ind+1}")
            printMat(m)
        m.switch(col,ind)


def convert_to_one(row,col,show=True,change_val=False):
    global m
    switch(show)
    R = m[row]/m[row][col]
    if show:
        if change_val:
            print(f"R{row+1} ==> R{row+1} / ({m[row][col]})")
        else:
            print(f"R{row+1}->R{row+1}/({m[row][col]})",R)

    if change_val:
        m[row] = R
    return R

def convert_to_zero(minus_row,row,col,show=True):
    global m
    R = convert_to_one(row,col,show=show,change_val=False)
    m[row] = R - minus_row
    if show:
        print(f"R{row+1} ==> R{row+1} - R{col+1}")
        printMat(m)


show = False
for col in range(len(m)-1):
    minus_row = convert_to_one(col,col,show=show)
    for row in range(1+col,len(m)):
        if float(m[row][col]) != 0:
            convert_to_zero(minus_row,row,col,show=show)

for col in range(len(m)):
    if m[col][col] != 1:
        convert_to_one(col,col,change_val=True,show=show)

printMat(m)
print("Result from Gaussian Elimination:")
printMat(m)
print("After Back-Substitution:")

ans = [Fraction(0) for _ in range(len(m))]
for i in range(-1,-len(m)-1,-1):
    total = vector([m[i][j]*ans[j+1] for j in range(-2,i-1,-1)])
    ans[i] = m[i][-1] - total.sum()

char = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(m)):
    print(f"{char[i]} = {ans[i]}")
