'''
# ==============================
# IMPORTS (DON'T TOUCH THIS)
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# LOAD DATA (CHANGE FILE NAME)
# ==============================
df = pd.read_excel("your_file.xlsx")

# ==============================
# BASIC EXPLORATION
# ==============================
print(df.head())
print(df.info())
print(df.describe())

# ==============================
# MISSING VALUES
# ==============================
print(df.isnull().sum())

# Drop missing rows
df_drop = df.dropna()

# Fill missing values (numeric)
df_fill = df.fillna(df.mean(numeric_only=True))

# Fill categorical with mode
for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)

# ==============================
# REMOVE DUPLICATES
# ==============================
df = df.drop_duplicates()

# ==============================
# STRING MANIPULATION
# ==============================
for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.strip().str.upper()

# ==============================
# DATA WRANGLING
# ==============================
# Example new column (edit as needed)
if 'Sales' in df.columns and 'Cost' in df.columns:
    df['Profit'] = df['Sales'] - df['Cost']

# Filtering
df_filtered = df[df.select_dtypes(include=np.number).columns[0]]

# Sorting
df_sorted = df.sort_values(by=df.select_dtypes(include=np.number).columns[0], ascending=False)

# ==============================
# GROUPBY (AGGREGATION)
# ==============================
if len(df.select_dtypes(include='object').columns) > 0:
    cat_col = df.select_dtypes(include='object').columns[0]
    num_col = df.select_dtypes(include=np.number).columns[0]
    print(df.groupby(cat_col)[num_col].sum())

# ==============================
# MERGING (IF MULTIPLE FILES)
# ==============================
# df2 = pd.read_excel("second_file.xlsx")
# merged = pd.merge(df, df2, on="common_column")

# ==============================
# OUTLIER DETECTION (IQR)
# ==============================
num_cols = df.select_dtypes(include=np.number)

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"Outliers in {col}:")
    print(outliers)

# ==============================
# VISUALIZATION
# ==============================
# Histogram
df[num_cols.columns[0]].hist()
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Bar chart (if categorical exists)
if len(df.select_dtypes(include='object').columns) > 0:
    cat_col = df.select_dtypes(include='object').columns[0]
    df[cat_col].value_counts().plot(kind='bar')
    plt.title("Bar Chart")
    plt.show()

# Scatter plot (if 2 numeric columns exist)
if len(num_cols.columns) >= 2:
    plt.scatter(df[num_cols.columns[0]], df[num_cols.columns[1]])
    plt.xlabel(num_cols.columns[0])
    plt.ylabel(num_cols.columns[1])
    plt.title("Scatter Plot")
    plt.show()

# ==============================
# SORTING & TOP VALUES
# ==============================
print(df.nlargest(5, num_cols.columns[0]))

# ==============================
# BASIC INSIGHTS (PRINTABLE)
# ==============================
print("Max value:", df[num_cols.columns[0]].max())
print("Min value:", df[num_cols.columns[0]].min())
print("Mean:", df[num_cols.columns[0]].mean())

# ==============================
# SAVE CLEANED DATA
# ==============================
df.to_csv("cleaned_data.csv", index=False)

# For Web Scraping
import requests
from bs4 import BeautifulSoup

# ==============================
# LOAD DATA (CHANGE FILE NAME)
# ==============================
df = pd.read_excel("your_file.xlsx")

# ==============================
# BASIC EXPLORATION
# ==============================
print(df.head())
print(df.info())
print(df.describe())

# ==============================
# MISSING VALUES
# ==============================
print(df.isnull().sum())

df = df.drop_duplicates()

# Fill numeric
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical
for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)

# ==============================
# STRING CLEANING
# ==============================
for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.strip().str.upper()

# ==============================
# DATA WRANGLING
# ==============================
if 'Sales' in df.columns and 'Cost' in df.columns:
    df['Profit'] = df['Sales'] - df['Cost']

# Sorting
num_col = df.select_dtypes(include=np.number).columns[0]
df_sorted = df.sort_values(by=num_col, ascending=False)

# ==============================
# GROUPBY
# ==============================
cat_cols = df.select_dtypes(include='object').columns
if len(cat_cols) > 0:
    print(df.groupby(cat_cols[0])[num_col].sum())

# ==============================
# MERGING (OPTIONAL)
# ==============================
# df2 = pd.read_excel("file2.xlsx")
# merged = pd.merge(df, df2, on="common_column")

# ==============================
# OUTLIER DETECTION (IQR)
# ==============================
for col in df.select_dtypes(include=np.number):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"Outliers in {col}:")
    print(outliers)

# ==============================
# VISUALIZATION
# ==============================
df[num_col].hist()
plt.title("Histogram")
plt.show()

if len(cat_cols) > 0:
    df[cat_cols[0]].value_counts().plot(kind='bar')
    plt.title("Bar Chart")
    plt.show()

if len(df.select_dtypes(include=np.number).columns) >= 2:
    cols = df.select_dtypes(include=np.number).columns
    plt.scatter(df[cols[0]], df[cols[1]])
    plt.xlabel(cols[0])
    plt.ylabel(cols[1])
    plt.title("Scatter Plot")
    plt.show()

# ==============================
# TOP VALUES
# ==============================
print(df.nlargest(5, num_col))

# ==============================
# SAVE CLEANED DATA
# ==============================
df.to_csv("cleaned_data.csv", index=False)

# ============================================================
# 🌐 WEBSCRAPING PART (IMPORTANT FOR YOUR PORTION)
# ============================================================

# ------------------------------
# Example 1: Scrape a simple webpage
# ------------------------------
url = "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    data = []

    for q, a in zip(quotes, authors):
        data.append({
            "Quote": q.text,
            "Author": a.text
        })

    df_web = pd.DataFrame(data)
    print(df_web.head())

# ------------------------------
# Example 2: Scrape table data
# ------------------------------
url2 = "https://www.worldometers.info/world-population/population-by-country/"

response2 = requests.get(url2)

if response2.status_code == 200:
    soup2 = BeautifulSoup(response2.text, "html.parser")

    table = soup2.find("table")
    rows = table.find_all("tr")[1:]  # skip header

    table_data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 0:
            table_data.append([col.text.strip() for col in cols])

    df_table = pd.DataFrame(table_data)
    print(df_table.head())

# ------------------------------
# Example 3: Save scraped data
# ------------------------------
df_web.to_csv("scraped_quotes.csv", index=False)


import numpy as np
from scipy import stats

# ==============================
# GRUBBS TEST (DETECT ONE OUTLIER)
# ==============================
def grubbs_test(data, alpha=0.05):
    data = np.array(data)
    n = len(data)

    mean = np.mean(data)
    std = np.std(data, ddof=1)

    deviations = abs(data - mean)
    max_dev = np.max(deviations)
    max_index = np.argmax(deviations)

    G = max_dev / std

    t_crit = stats.t.ppf(1 - alpha/(2*n), n-2)
    G_crit = ((n-1)/np.sqrt(n)) * np.sqrt(t_crit**2 / (n-2 + t_crit**2))

    print("G calculated:", G)
    print("G critical:", G_crit)

    if G > G_crit:
        print("Outlier detected:", data[max_index])
    else:
        print("No outlier detected")


# ==============================
# GRUBBS TEST (REMOVE OUTLIERS ITERATIVELY)
# ==============================
def grubbs_remove(data, alpha=0.05):
    data = list(data)

    while True:
        arr = np.array(data)
        n = len(arr)

        mean = np.mean(arr)
        std = np.std(arr, ddof=1)

        deviations = abs(arr - mean)
        max_dev = np.max(deviations)
        max_index = np.argmax(deviations)

        G = max_dev / std

        t_crit = stats.t.ppf(1 - alpha/(2*n), n-2)
        G_crit = ((n-1)/np.sqrt(n)) * np.sqrt(t_crit**2 / (n-2 + t_crit**2))

        if G > G_crit:
            print("Removing outlier:", arr[max_index])
            data.pop(max_index)
        else:
            break

    return data


# ==============================
# EXAMPLE USAGE
# ==============================
data = [10, 12, 13, 12, 11, 14, 13, 100]

print("=== Grubbs Test ===")
grubbs_test(data)

print("\n=== Removing Outliers ===")
cleaned = grubbs_remove(data)
print("Cleaned data:", cleaned)
  
'''
