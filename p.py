"""

#  FUNCTIONS
def add(a,b=0): return a+b
def fact(n): return 1 if n==0 else n*fact(n-1)
square = lambda x: x*x
def test(*args, **kwargs): pass


#  DECORATORS & WRAPPERS
def deco(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@deco
def greet(): print("Hello")
greet()


#  CLASSES & OBJECTS
class Student:
    def __init__(self,name,marks):
        self.name=name; self.marks=marks
    def display(self): print(self.name,self.marks)

s1=Student("Arun",90)
s1.display()

class Animal:
    def speak(self): print("sound")
class Dog(Animal):
    def speak(self): print("bark")
Dog().speak()


#  NUMPY QUICK REFERENCE
import numpy as np

a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
np.zeros((2,3)); np.ones((3,3)); np.eye(3)
np.arange(0,10,2); np.linspace(0,1,5)

a+b; a*b; np.dot(a,b)
np.sum(a); np.mean(a); np.std(a)
np.reshape(a,(3,1)); a.flatten()
np.random.randint(1,10,(2,2))
np.linalg.inv(b); np.linalg.det(b)


#  2D / 3D / 4D ARRAYS
a2=np.arange(9).reshape(3,3)
a3=np.arange(24).reshape(2,3,4)
a4=np.random.randint(1,10,(2,2,2,2))
a2[:,0]; a3[1,:,:]; a4[0,1,:,:]


#  MATPLOTLIB
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1); y=np.sin(x)
plt.plot(x,y,'r--',label='sinx')
plt.xlabel('x'); plt.ylabel('y')
plt.title('Sine Wave'); plt.legend(); plt.show()

plt.bar(['A','B','C'],[10,20,15])
plt.scatter([1,2,3],[4,5,6])
data=np.random.randn(1000)
plt.hist(data,bins=20)

fig,ax=plt.subplots(2,2)
ax[0,0].plot(x,y)


# 2D / 3D Visualization
plt.imshow(np.random.randint(0,10,(5,5)),cmap='viridis')
plt.colorbar()

from mpl_toolkits.mplot3d import Axes3D
X,Y=np.meshgrid(np.linspace(-5,5,50),np.linspace(-5,5,50))
Z=np.sin(np.sqrt(X**2+Y**2))
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap='plasma')
plt.show()


# PANDAS
import pandas as pd

s=pd.Series([10,20,30],index=['a','b','c'])
data={'Name':['A','B'],'Age':[20,25]}
df=pd.DataFrame(data)
df.head(); df.info(); df.describe()
df['Age'].mean(); df.loc[0]; df.iloc[1,0]
pd.read_csv('file.csv'); df.to_csv('out.csv',index=False)
df.groupby('Name')['Age'].mean()
df.fillna(0); df.dropna()


#  SCIPY
from scipy import stats, linalg, integrate

data=[1,2,3,4,5]
print(stats.mean(data))
print(stats.mode(data))
print(stats.pearsonr([1,2,3],[2,4,6]))

A=np.array([[1,2],[3,4]]); b=np.array([5,6])
x=linalg.solve(A,b)
res=integrate.quad(lambda x: x**2,0,2)
print(res)


#  COMMON EXAM PROGRAMS
def fib(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=' ')
        a,b=b,a+b

def is_armstrong(n):
    s=sum(int(d)**len(str(n)) for d in str(n))
    return s==n

def is_perfect(n):
    return sum(i for i in range(1,n) if n%i==0)==n

def is_prime(n):
    if n<2:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True

def sum_div(n):
    return sum(i for i in range(1,n) if n%i==0)
for a in range(2,10000):
    b=sum_div(a)
    if b>a and sum_div(b)==a: print(a,b)

for i in range(3,50,2):
    if is_prime(i) and is_prime(i+2): print(i,i+2)


#  STRING & PATTERN QUICKIES
s=input("Enter:")
print(s[::-1])
print(sorted(s))
print(len(s))

for i in range(7):
    for j in range(5):
        if j==0 or j==4 or i==3:
            print("*",end=" ")
        else: print(" ",end=" ")
    print()


# PACKAGES / MODULES
# Folder structure:
# mathe/
#  ├── __init__.py
#  ├── add.py
#  └── mult.py
# main.py

# add.py
def add_lists(a,b):
    return sorted([x+y for x,y in zip(a,b)])

# mult.py
def mult_lists(a,b):
    return sorted([x*y for x,y in zip(a,b)])

# main.py
from mathe import add, mult
a=[1,2,3]; b=[4,5,6]
print(add.add_lists(a,b))
print(mult.mult_lists(a,b))


#  QUICK REMINDERS
# np.arange() → create ranges
# plt.subplots() → multiple plots
# pd.DataFrame() → tabular data
# stats, linalg in scipy → math functions
# @decorator → wraps a function
# self → refers to current object in class

"""

