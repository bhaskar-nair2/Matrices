##Just import m1 and use m1.functions to use the functions, a sample is shown in main.py file

##r=Rows;
##c=Cols;
##a=Matrix1;
##x=Matrix Unknown;
##b=Matrix2;
##n=NewMatrix;
##RE=Result;
##v=Value

# INput
def in_by_val():
    n=[]
    print("All numbers seperate by ' ' space")
    r=int(input("Matrix Rows: "))
    c=int(input("Matrix Cols: "))
    print("Now Input the Matrix")
    for _ in range(0,r):
        n.append(input().split(' '))
        if(len(n[_])!=c):
            print("Error: Wrong Cols/Please split values")
            break
    x=n
    n=[]
    return x

## Errors
class Error(Exception):
    pass
class inden_Err(Error):
    pass
def rechk():
    print("Unnatural Matrix Sizes\nFor Matrix AxB \
              \nColumns of A should be equal to Rows of B\
              \nPlease re-check your Input\n more info at \
              https://www.youtube.com/watch?v=FX4C-JpTFgY")
#Checks
def can_be(a,b):
    if len(a[0])==len(b):
        return True
    else:
        return False
def mat_type(a,b):
    if len(a)==len(b) and len(a[0])==len(b[0]):
        return True
    else:
        return False
def mat_def(a,b):
    if can_be(a,b):
        if mat_type(a,b):
            return 1
        else:
            return 2
    else:
        raise inden_Err

#Multiplication
def even_mul_mat(a,b):
    v=0
    n=[]
    RE=[]
    r=len(a)
    c=len(b[1]) ## for matXmat  (3*(2) X (2)*3)

    for i in range(0,r):
        for k in range(0,r):#range is not inclusive
            for j in range(0,c):
                v=v+(int(a[i][j])*int(b[j][k]))
            n.append(v)
            v=0
        RE.append(n)
        n=[]
    return RE
def uneven_mat_mul(a,b):
    v1=0
    v2=0
    n=[]
    RE=[]
    r1=len(a)
    r2=len(b)
    c1=len(a[0])#c1==r2
    c2=len(b[0])

    for i in range(0,r1):
        for j in range(0,c2):
            for k in range(0,c1):
                v1=v1+(int(a[i][k])*int(b[k][j]))
            n.append(v1)
            v1=0
        RE.append(n)
        n=[]
    print(RE)
                    
def fin(a,b):
    try:
        if mat_def(a,b)==1:
            print(even_mul_mat(a,b))
        else:
            uneven_mat_mul(a,b)
    except inden_Err:
        rechk()
