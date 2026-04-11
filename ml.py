#exp 2 
df.hist(bins=20,figsize=(10,10),color = 'green')
plt.suptitle("Histogram for each attribute")
plt.show()

#boxplot 
fig,axs = plt.subplots(9,1,figsize=(10,20))
i = 0
for col in df.columns:
  axs[i].boxplot(df[col],vert=False)
  axs[i].set_ylabel(col)
  i += 1
plt.show()

df.boxplot(figsize=(20,10))
plt.show()

#heat map
corr = df.corr()
sns.heatmap(corr,fmt='.2f',annot=True,cmap='coolwarm')
plt.show()


#pie
plt.pie(df['Outcome'].value_counts(),labels=['No Diabetes','Diabetes'],autopct='%1.1f%%',explode=[0.05,0])
plt.title("Outcome proportionality")
plt.show()

#minmax
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
rescaledx = scaler.fit_transform(x)
rescaledx[:5]
#zscore
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(x)
rescaledx = scaler.fit_transform(x)
rescaledx[:5]
#preprocessing pipeline

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
numerical_df=df.select_dtypes(include=['int64','float64']).columns
numeric_transformer=Pipeline([('impute',SimpleImputer(missing_values=np.nan,strategy='mean')),('scale',StandardScaler())])
preprocessor_pipeline=ColumnTransformer(transformers=[('num',numeric_transformer,numerical_df)])
preprocessor_pipeline.fit(df)
df_data=preprocessor_pipeline.transform(df)
df_data

#underfitting and overfitting
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# Generate data (ONLY ONCE)
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.3, size=x.shape)
x_reshaped = x.reshape(-1, 1)

# Function to train and plot
def train_and_plot(model, title):
    model.fit(x_reshaped, y)
    y_pred = model.predict(x_reshaped)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, label='data')
    plt.plot(x, y_pred, label=title)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Underfitting (Linear)
linear_model = LinearRegression()
train_and_plot(linear_model, 'Underfitting (Linear Regression)')

# Overfitting (Polynomial)
poly_model = make_pipeline(PolynomialFeatures(degree=15), LinearRegression())
train_and_plot(poly_model, 'Overfitting (Polynomial Degree 15)')


"""
Experiment: Grid Search & Random Search on SVM (Iris Dataset)

Objective:
Tune hyperparameters of SVM using GridSearchCV and RandomizedSearchCV
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define model
svm = SVC()

# Hyperparameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto']
}

# ------------------ GRID SEARCH ------------------
grid_search = GridSearchCV(
    estimator=svm,
    param_grid=param_grid,
    cv=5,
    verbose=1
)

grid_search.fit(X_train, y_train)

print("\n🔹 Grid Search Best Parameters:")
print(grid_search.best_params_)

# Test accuracy
y_pred_grid = grid_search.predict(X_test)
print("Grid Search Accuracy:", accuracy_score(y_test, y_pred_grid))


# ------------------ RANDOM SEARCH ------------------
param_dist = {
    'C': np.linspace(0.1, 100, 50),
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto']
}

random_search = RandomizedSearchCV(
    estimator=svm,
    param_distributions=param_dist,
    n_iter=10,   # tries 10 random combinations
    cv=5,
    random_state=42,
    verbose=1
)

random_search.fit(X_train, y_train)

print("\n🔹 Random Search Best Parameters:")
print(random_search.best_params_)

# Test accuracy
y_pred_random = random_search.predict(X_test)
print("Random Search Accuracy:", accuracy_score(y_test, y_pred_random))

#PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

np.random.seed(68)
x = np.random.randint(100,size=(100,3))
x_df = pd.DataFrame(x)
print(x_df.head())

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_df)
x_scaled_df = pd.DataFrame(x_scaled)
print(x_scaled_df.head())

pca = PCA(n_components=2)
pca.fit(x_scaled)
x_pca = pca.transform(x_scaled)
x_pca_df = pd.DataFrame(x_pca)
print(x_pca_df)

variance_explained = pca.explained_variance_ratio_
print(f'variance explained {variance_explained}')
cumulative_variance_explained = np.cumsum(variance_explained)
print(f'cumulative variance explained {cumulative_variance_explained}')

plt.plot(range(1,len(cumulative_variance_explained)+1),cumulative_variance_explained,marker ='o')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance Ratio')
plt.title("Cumulative Variance Ratio vs Number of Principal Components")
plt.show()

#confusion matrix
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# Actual and Predicted values
y_true = ['Cat','Cat','Dog','Dog','Horse','Horse','Cat','Dog','Horse','Cat']
y_pred = ['Cat','Dog','Dog','Dog','Horse','Cat','Cat','Dog','Horse','Horse']

# Class labels
classes = ['Cat', 'Dog', 'Horse']

# Create confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=classes)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=classes)
disp.plot(cmap=plt.cm.Blues)

# Labels and title
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification report
print("Classification Report:\n")
print(classification_report(y_true, y_pred))

#k-means clustering
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x=[5,6,12,5,4,13,15,7,10,14]
y=[21,19,24,17,16,25,24,22,21,21]
data=list(zip(x,y))

kmean = KMeans(n_clusters=2)
kmean.fit(data)
centroids = kmean.cluster_centers_
labels = kmean.labels_

plt.scatter(x,y,c=labels)
plt.scatter(centroids[:,0],centroids[:,1],s=200,c='darkred')

#AGNES clustering
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram,linkage

singleLinkage = linkage(data,method='single', metric='euclidean')
dendrogram(singleLinkage)
plt.title('single Linkage')
plt.show()

completeLinkage  = linkage(data,method='complete',metric='euclidean')
dendrogram(completeLinkage)
plt.title("Complete Linkage")
plt.show()

agnes = AgglomerativeClustering(n_clusters=2,linkage='complete')
agnes.fit(data)
labels = agnes.fit_predict(data)
print(labels)
plt.scatter(x,y,c=labels)


#replace outliers
def replace_outliers(col):
    Q1 = col.quantile(0.25)
    Q3 = col.quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    mean_val = col[(col >= lower) & (col <= upper)].mean()

    return col.apply(lambda x: mean_val if x < lower or x > upper else x)


df['num1'] = replace_outliers(df['num1'])
df['num2'] = replace_outliers(df['num2'])
df['num3_discrete'] = replace_outliers(df['num3_discrete'])
