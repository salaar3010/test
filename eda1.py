''' 
#data visualization
bin_edges =[i for i in range(0,160,10)]
plt.hist(df['Speed'],bins=bin_edges,color='green',edgecolor='black')
plt.xlabel('Pokemon Speed')
plt.ylabel('Frequency')
plt.show()

sns.set_style()
sns.distplot(df['Speed'],color='purple')
plt.show()

sns.displot(df['Speed'],color='orange')
plt.show()

sns.lmplot(x='Attack',y='Defense',data=df)

sns.lmplot(x='Attack',y='Defense',data=df,fit_reg=False,hue='Stage')

sns.catplot(x='Type 1',
            y='Attack',
            data = df,
            hue='Stage',
            col='Stage',
            kind='swarm',
            height=5,
            aspect=1.2)

sns.violinplot(x='Type 1',y='Attack',data=df,palette='Set2')

sns.swarmplot(x='Type 1',y='Attack',data=df,palette='Set2')
sns.violinplot(x='Type 1',y='Attack',data=df,inner=None,palette='Set2')

numeric_values=df1.select_dtypes(include=[np.number])
numeric_values.columns
sns.heatmap(numeric_values.corr(),annot=True,cmap='RdYlGn')

#file handling 

file = open("name.txt",'w')
file.write("Hey, there!")
file.close()

with open('name.txt','r') as f:
    print(f.read())

file.close()

with open("file1.txt",'w') as f:
    f.write("Something \n")
    f.write("Below")
    
with open("file1.txt",'r') as f:
    print(f.read())


#outlier detection using boxplot
import sklearn
from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Diabetes = load_diabetes()
column_name = Diabetes.feature_names
Diabetes_df = pd.DataFrame(Diabetes.data, columns=column_name)
sns.boxplot(Diabetes_df['bmi'])
plt.title('Boxplot of BMI')
plt.show()

def removal_box_plot(df,column,threshold):
  removed_outliers = df[df[column] < threshold]
  sns.boxplot(removed_outliers[column])
  plt.title(f'Boxplot without Outliers of {column}')
  plt.show()
  return removed_outliers

removal_box_plot(Diabetes_df,'bmi',0.12)

fig,ax = plt.subplots(figsize=(6,4))
ax.scatter(Diabetes_df['bmi'],Diabetes_df['bp'])
ax.set_xlabel('BMI')
ax.set_ylabel('BP')
plt.title('Scatterplot of BMI and BP')
plt.show()

outlier_indices = np.where((Diabetes_df['bmi']>0.12)&(Diabetes_df['bp'] < 0.8))
no_outlier=Diabetes_df.drop(outlier_indices[0])

fig,ax_no_outliers = plt.subplots(figsize=(6,4))
ax_no_outliers.scatter(no_outlier['bmi'],no_outlier['bp'])
ax_no_outliers.set_xlabel('BMI')
ax_no_outliers.set_ylabel('BP')
plt.title('Scatterplot of BMI and BP without Outliers')
plt.show()

from scipy import stats
z = np.abs(stats.zscore(Diabetes_df['age']))
print(z)

threshold_z = 2
outlier_indices_z = np.where(z > threshold_z)[0]
no_outlier_z=Diabetes_df.drop(outlier_indices_z)
print("Orginal Datafram Shape",Diabetes_df.shape)
print("Dataframe Shape after removing outliers",no_outlier_z.shape)

q1 = np.percentile(Diabetes_df['bmi'],25,method ='midpoint')
q3 = np.percentile(Diabetes_df['bmi'],75,method ='midpoint')
IQR = q3 - q1
upper = q3 + 1.5*IQR
lower = q1 - 1.5*IQR
print(IQR

upper_array= np.array(Diabetes_df['bmi'] >= upper)
print("Upper bound", upper)
print(upper_array.sum())
lower_array= np.array(Diabetes_df['bmi'] <= lower)
print("Lower bound", lower)
print(lower_array.sum())


'''
