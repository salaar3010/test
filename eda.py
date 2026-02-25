#exp - 7
import numpy as np
import pandas as pd
previous_max_rows=pd.options.display.max_rows
pd.options.display.max_rows=25
pd.options.display.max_columns=20
pd.options.display.max_colwidth=82
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure',figsize=(10,6))
np.set_printoptions(precision=4,suppress=True)

string_data=pd.Series(['aardvark',np.nan,None,'avacodo'])
print(string_data)
string_data.isna()

float_data=pd.Series([1,2,None],dtype='float64')
print(float_data)
float_data.isna()

data=pd.Series([1,np.nan,3.5,np.nan,7])
data.dropna()

data=pd.DataFrame([[1.,6.5,3.],[1.,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,3.]])
data
print(data)
data.dropna()
data.dropna(how='all')

data[4]=np.nan
data
data.dropna(axis='columns',how='all')

df=pd.DataFrame(np.random.standard_normal((7,3)))
df.iloc[:4,1]=np.nan
df.iloc[:2,2]=np.nan
df
df.dropna()
df.dropna(thresh=2)

df.fillna(0)

data=pd.Series([1.,np.nan,3.5,np.nan,7])
data.fillna(data.mean())

data=pd.Series([2,np.nan,3,4,5,6])
data.fillna(data.median())

data=pd.Series([2,np.nan,2,3,5,6])
data.fillna(data.mode())

data=pd.DataFrame({'jersey no':[7,18,45,17,8],'player':['dhoni','virat','rohit','ab de villiers','jadeja']})

data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Q1 Sales': [150, 200, 250, 300],
    'Q2 Sales': [180, 220, 270, 320],
    'Q3 Sales': [200, 240, 290, 350]
}
df = pd.DataFrame(data)
df.set_index('Product', inplace=True)
ax = df.plot(kind='bar', stacked=True, figsize=(8, 6))
plt.title('Quarterly Sales by Product')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.legend(title='Quarter')
plt.xticks(rotation=45)


# exp 4
fo = open("foo.txt",'wb')
print ("Name of the file: ",fo.name)
print("Closed or not: ",fo.closed)
print("Opening mode",fo.mode)

file = open("name.txt",'w')
file.write("Hey, there!")
file.close()

with open('name.txt','r') as f:
    print(f.read())

with open("file1.txt",'w') as f:
    f.write("Something \n")
    f.write("Below")

with open("file1.txt",'r') as f:
    print(f.read())

with open('file1.txt','a') as f:
    f.write('Place holder TT\n')

with open('file1.txt','r') as f:
    print(f.read())

import pandas as pd
df = pd.read_csv('data.csv')
print(df)

df.to_csv('output.csv',index=False)
df.to_excel('data.xlsx',index=False)
df = pd.read_excel('data.xlsx')
print(df)

import random
DM= {"Name":['Guru','Siva','Bhags','Charan','partha','dipak','vedha','yuga','nesa','ram',
             'sita','nithesh','rebin','harish','rithish','lux','warwick','aatrox','Praboss','naveen'],
     'rice':[random.choice([0,1]) for _ in range(20)],
     'chilli':[random.choice([0,1]) for _ in range(20)],
     'badam':[random.choice([0,1]) for _ in range(20)],
     'sunflower oil':[random.choice([0,1]) for _ in range(20)],
     'Milk':[random.choice([0,1]) for _ in range(20)]
     }
data = pd.DataFrame(DM,index=[i for i in range(1,21)])
data.to_csv('Rice_Traders.csv')
data.to_excel('Rice_Traders.xlsx')
data.head()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path =r'/content/Virat-Kohli-International-Cricket-Centuries.csv'
virat_df = pd.read_csv(path)
virat_df

virat_df_stats = pd.get_dummies(virat_df['Result'])

result_counts = virat_df_stats.sum()
plt.figure(figsize=(10, 6))
plt.bar(result_counts.index, result_counts.values,color='green')
plt.xlabel('Match Result')
plt.ylabel('Number of Centuries')
plt.title('Virat Kohli Century Match Results')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#exp 5
df = pd.read_csv(r"C:\DM Drive\VIT Sem 2\EDA\EDA activiy 1.csv")
df.head()
df.shape
df.dtypes

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
numerical_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()

df['customerID'].duplicated().sum()
df.isnull().sum()

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges']= df['TotalCharges'].fillna(df['TotalCharges'].median())

df['gender'] = df['gender'].str.strip().str.capitalize()

df[['tenure','MonthlyCharges','TotalCharges']].mean()

df[['SeniorCitizen','Partner','Dependents']].value_counts()
df['SeniorCitizen'].value_counts()
df['Partner'].value_counts()
df['Dependents'].value_counts()

(df['PaperlessBilling'].value_counts(normalize=True) * 100)

df['InternetService'].value_counts()
pd.crosstab(df['InternetService'], df['Churn'], normalize='index') * 100

plt.hist(df['tenure'])
plt.hist(df['MonthlyCharges'])
plt.hist(df['TotalCharges'])

df['Churn'].value_counts().plot(kind='bar')
pd.crosstab(df['Contract'], df['Churn']).plot(kind='bar', stacked=True)
pd.crosstab(df['InternetService'], df['Churn']).plot(kind='bar', stacked=True)
pd.crosstab(df['PaymentMethod'], df['Churn']).plot(kind='bar', stacked=True)


#exp 3
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('/content/ds-1.csv',encoding='ISO-8859-1',index_col=0)
df.shape
df.head(149)
df.describe()

plt.hist(df['Speed'],histtype='bar',bins=20,color='red',edgecolor='black')
bin_edges =[i for i in range(0,160,10)]
plt.hist(df['Speed'],bins=bin_edges,color='green',edgecolor='black')

sns.distplot(df['Speed'],color='purple')
sns.displot(df['Speed'],color='orange')
sns.lmplot(x='Attack',y='Defense',data=df)
sns.scatterplot(x='Attack',y='Defense',data=df)
sns.lmplot(x='Attack',y='Defense',data=df,fit_reg=False,hue='Stage')

sns.catplot(x='Type 1',y='Attack',data=df,hue='Stage',col='Stage',kind='swarm')
sns.boxplot(data=df)

stats_df = df.drop(['Total','Stage','Legendary'],axis=1)
sns.boxplot(data=stats_df)

sns.violinplot(x='Type 1',y='Attack',data=df,palette='Set2')
sns.swarmplot(x='Type 1',y='Attack',data=df,palette='Set2')

plt.figure(figsize=(10,6))
sns.violinplot(x='Type 1',y='Attack',data=df,inner=None,palette='Set2')

#exp 6
from sklearn.datasets import load_diabetes
Diabetes = load_diabetes()
column_name = Diabetes.feature_names
Diabetes_df = pd.DataFrame(Diabetes.data, columns=column_name)

sns.boxplot(Diabetes_df['bmi'])

def removal_box_plot(df,column,threshold):
  removed_outliers = df[df[column] < threshold]
  sns.boxplot(removed_outliers[column])
  return removed_outliers

removal_box_plot(Diabetes_df,'bmi',0.12)

fig,ax = plt.subplots()
ax.scatter(Diabetes_df['bmi'],Diabetes_df['bp'])

outlier_indices = np.where((Diabetes_df['bmi']>0.12)&(Diabetes_df['bp'] < 0.8))
no_outlier=Diabetes_df.drop(outlier_indices[0])

fig,ax_no_outliers = plt.subplots()
ax_no_outliers.scatter(no_outlier['bmi'],no_outlier['bp'])

from scipy import stats
z = np.abs(stats.zscore(Diabetes_df['age']))

threshold_z = 2
outlier_indices_z = np.where(z > threshold_z)[0]
no_outlier_z=Diabetes_df.drop(outlier_indices_z)

q1 = np.percentile(Diabetes_df['bmi'],25,method ='midpoint')
q3 = np.percentile(Diabetes_df['bmi'],75,method ='midpoint')
IQR = q3 - q1
upper = q3 + 1.5*IQR
lower = q1 - 1.5*IQR

upper_array= np.array(Diabetes_df['bmi'] >= upper)
lower_array= np.array(Diabetes_df['bmi'] <= lower)

Diabetes_df.drop(index=upper_array,inplace=True)
Diabetes_df.drop(index=lower_array,inplace=True)