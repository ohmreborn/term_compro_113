
# Students don't submit this code to elab

# ใช้ newton methods ในการประมาณค่า square root แล้วจัดรูปนิดหน่อยเพราะคำนวณแบบนี้มันเร็วกว่าเพราะอะไรไม่รู้
# https://en.wikipedia.org/wiki/Newton%27s_method
def square_root(a,l=10**-6):
    x = a
    while abs(x**2 - a) >=l:
        x = (x + a/x)*0.5
    return x

"""
อีกอันจำไม่ได้ เพราะไม่ได้ทำ
"""
