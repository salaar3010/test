'''
🧮 NumPy Notes 
1. Import
import numpy as np
2. Array Creation
np.array([1,2,3])                   # 1D array
np.array([[1,2,3],[4,5,6]])         # 2D array
arr3d = np.array([[[1,2,3], # 3d array
                   [4,5,6]],
            
                  [[7,8,9],
                   [10,11,12]]])

np.zeros((3,3))                     # 3x3 zeros
np.ones((2,4))                      # 2x4 ones
np.eye(3)                           # Identity matrix
np.arange(0,10,2)                   # [0 2 4 6 8]
np.linspace(0,1,5)                  # [0. 0.25 0.5 0.75 1.]
np.random.rand(3,2)                 # random floats
np.random.randint(1,10,5)           # random ints
3. Array Info
arr.shape                           # shape (rows, cols)
arr.size                            # total elements
arr.ndim                            # number of dimensions
arr.dtype                           # data type
4. Reshape & Flatten
arr.reshape(3,2)
arr.flatten()
5. Indexing & Slicing
arr[0]                              # first row
arr[:,1]                            # 2nd column
arr[1,2]                            # element at row1,col2
arr[1:3, 0:2]                       # slicing rows & cols
arr3d[0]             # first 2D block
arr3d[1, 0]          # row 0 of 2nd block
arr3d[1, 1, 2]       # specific element (12)
arr3d[:, 0, :]        # all blocks, first row
arr3d[0, :, 1:]  
6. Math Operations
arr + 10
arr - 5
arr * 2
arr / 2
np.add(arr1, arr2)
np.subtract(arr1, arr2)
np.multiply(arr1, arr2)
np.divide(arr1, arr2)
np.sqrt(arr)
np.exp(arr)
np.log(arr)
7. Aggregations
np.sum(arr)
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.min(arr)
np.max(arr)
np.argmax(arr)
np.argmin(arr)
8. Transpose & Dot Product
arr.T
np.dot(arr1, arr2)
9. Stack & Concatenate
np.hstack((a,b))
np.vstack((a,b))
np.concatenate((a,b), axis=0)
10. Boolean Operations
arr > 5
np.where(arr > 5, 1, 0)
np.unique(arr)


🧾 Pandas Notes (Syntax Focus)
1. Import
import pandas as pd
2. Series
s = pd.Series([10,20,30], index=['a','b','c'])
s['a']
s.values
s.index
3. DataFrame Creation
df = pd.DataFrame({'Name':['Siva','Raj'], 'Age':[21,22]})
4. Read / Write
pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)
5. Data Inspection
df.head()             # first 5 rows
df.tail(3)            # last 3 rows
df.shape
df.info()
df.describe()
df.columns
df.dtypes
6. Column & Row Operations
df['Name']                            # select column
df[['Name','Age']]                    # multiple columns
df.loc[0]                             # select row by label
df.iloc[1]                            # select row by index
df.loc[0,'Name']                      # single element
df.iloc[0,1]
7. Filtering
df[df['Age'] > 20]
df[(df['Age'] > 20) & (df['Age'] < 25)]
8. Add / Update / Drop Columns
df['City'] = ['Chennai','Salem']
df.drop('City', axis=1, inplace=True)
df.rename(columns={'Name':'FullName'}, inplace=True)
9. Sorting
df.sort_values(by='Age', ascending=False)
10. Handling Missing Data
df.isnull()
df.notnull()
df.dropna()
df.fillna(0)
11. Aggregation
df['Age'].mean()
df['Age'].max()
df['Age'].min()
df['Age'].sum()
12. GroupBy
df.groupby('City')['Age'].mean()
13. Merge / Join / Concat
pd.concat([df1, df2], axis=0)
pd.merge(df1, df2, on='ID')
14. Apply Functions
df['Age'].apply(lambda x: x+1)
15. Export
df.to_excel('file.xlsx', index=False)





📊 Matplotlib Notes (Syntax Focus)
1. Import
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # optional in newer versions
import numpy as np
2. Basic Line Plot
plt.plot(x, y)
plt.title('Title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
3. Multiple Lines
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.legend()
plt.show()
4. Scatter Plot
plt.scatter(x, y)
plt.show()
5. Bar Chart
plt.bar(x, y)
plt.barh(x, y)
plt.show()
6. Histogram
plt.hist(data, bins=10)
plt.show()
7. Pie Chart
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.show()
8. Subplots
plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.bar(x,y)
plt.show()
9. Styling
plt.grid(True)
plt.xlim(0,10)
plt.ylim(0,20)
plt.style.use('ggplot')
10. Save Plot
plt.savefig('plot.png')

🧠 Quick Combined Practice
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy
arr = np.random.randint(1,10,(3,3))
print(arr.mean(), arr.T)

# Pandas
df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
print(df.describe())
df['C'] = df['A'] + df['B']

# Matplotlib
plt.plot(df['A'], df['B'])
plt.title('Line Plot')
plt.show()




Pie Chart explode 

import matplotlib.pyplot as plt

# Data
values = [40, 25, 20, 15]
labels = ['Python', 'C', 'Java', 'C++']

# Explode one slice (Python)
explode = [0.1, 0, 0, 0]   # only first slice is exploded

# Plot
plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Programming Language Popularity')
plt.show()



3d ploting
Perfect, Siva 💪
Here’s a quick, exam-focused guide for your 3D arrays and 3D plotting in Python, keeping it short, syntax-based, and lab-ready 👇
________________________________________
🧮 NumPy 3D Arrays
1. Creating a 3D Array
import numpy as np

arr3d = np.array([[[1,2,3],
                   [4,5,6]],
                  
                  [[7,8,9],
                   [10,11,12]]])
✅ Shape → (2, 2, 3)
→ 2 blocks (depth), each having 2 rows × 3 columns
________________________________________
2. Accessing Elements
arr3d[0]             # first 2D block
arr3d[1, 0]          # row 0 of 2nd block
arr3d[1, 1, 2]       # specific element (12)
________________________________________
3. Shape, Dimensions, Size
arr3d.shape           # (2, 2, 3)
arr3d.ndim            # 3
arr3d.size            # 12 elements
________________________________________
4. Reshape a 3D Array
arr = np.arange(27).reshape(3,3,3)
________________________________________
5. Slicing
arr3d[:, 0, :]        # all blocks, first row
arr3d[0, :, 1:]       # first block, all rows, skip first column
________________________________________
6. Math Operations
arr3d + 5
np.mean(arr3d)
np.sum(arr3d, axis=0)   # sum along depth
________________________________________
📊 3D Plotting (Matplotlib)
Use Axes3D or ax = plt.axes(projection='3d') for 3D plots.
________________________________________
1. Setup
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # optional in newer versions
import numpy as np
________________________________________
2. Create a 3D Axes
fig = plt.figure()
ax = plt.axes(projection='3d')
________________________________________
3. 3D Scatter Plot
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

ax.scatter3D(x, y, z, color='blue')
plt.title('3D Scatter Plot')
plt.show()
________________________________________
4. 3D Line Plot
z = np.linspace(0, 1, 100)
x = z * np.sin(25*z)
y = z * np.cos(25*z)

ax.plot3D(x, y, z, 'green')
plt.title('3D Line Plot')
plt.show()
________________________________________
5. 3D Surface Plot
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title('3D Surface Plot')
plt.show()
________________________________________
6. 3D Wireframe Plot
ax.plot_wireframe(X, Y, Z, color='orange')
plt.title('3D Wireframe')
plt.show()
________________________________________
7. Add Labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
________________________________________
from scipy import stats
import  matplotlib.pyplot as plt 
import numpy as np
#linear regression
x =np.array( [1,2,3])
y = [5,7,9]

res = stats.linregress(x,y)
plt.plot(x,y,'o')
plt.plot(x,res.slope*x + res.intercept,'r')
plt.show()
#stats


'''
