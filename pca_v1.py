# -*- coding: utf-8 -*-
"""PCA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15EnAr7SjcxE_2kHhUIwMu1SmKYLRKzcH
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('/home/machine/Desktop/ML_Lab/wine.csv')
df.head()

df_shuffled = df.sample(frac=1, random_state=42)
df_shuff = df.sample(frac=1,random_state=42)

df_shuffled.head()

X = df.drop('Wine',axis=1)
y = df['Wine']
n_samples,n_features = X.shape
print('n_samples: ',n_samples,' n_features: ',n_features)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

"""### Initial Data Visualization"""

plt.figure(figsize=(10,6))
plt.scatter(df['OD'],df['Flavanoids'],c=df['Wine'],edgecolors='k',alpha=0.75,s=150)
plt.grid(True)
plt.title("Scatter plot of OD and Flavanoids features showing their \ncorrelation and class seperation",fontsize=15)
plt.xlabel("OD",fontsize=15)
plt.ylabel("Flavanoids",fontsize=15)
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['Alcohol'],df['Ash'],c=df['Wine'],edgecolors='k',alpha=0.75,s=150)
plt.grid(True)
plt.title("Scatter plot of the Alcohol and Ash features showing their \ncorrelation and class seperation",fontsize=15)
plt.xlabel("Alcohol",fontsize=15)
plt.ylabel("Ash",fontsize=15)
plt.show()

"""### Data Preprocessing"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)

from sklearn.decomposition import PCA
pca = PCA()
final_wine = pca.fit_transform(X)  #performing eigen decomposition followed by projection

#displaying the variance captured by PCA
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

#Rounding off the variances to fewer decimal places
rounded_var=np.round(pca.explained_variance_,1)
plt.figure(figsize=(10,7))
pca_components = [i+1 for i in range(len(rounded_var))]
plt.scatter(pca_components,rounded_var,edgecolors='k',alpha=0.75,s=150)
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance obtained after PCA')
plt.title('Variance vs Component after PCA')
plt.xticks(np.arange(pca_components[0],pca_components[len(pca_components)-1]+1,1))
plt.show()

#Variance captured using first two principal components
var = np.sum(pca.explained_variance_[0:2])
print(np.round(var,2))
var_percentage = np.sum(pca.explained_variance_ratio_[0:2])*100
print(np.round(var_percentage,2),'%')

"""### Data Visualization after PCA"""

figure = plt.figure()
ax = plt.gca()
plt.scatter(final_wine[:,0],final_wine[:,1], c=df['Wine'], edgecolor='none', alpha=0.5)
ax.set_title("The PCA plot")
ax.set_xlabel("The first principle component")
ax.set_ylabel("The second principle component")

figure = plt.figure()
ax = plt.gca()
plt.scatter(final_wine[:,2],final_wine[:,3], c=df['Wine'], edgecolor='none', alpha=0.5)
ax.set_title("The PCA plot")
ax.set_xlabel("The third principal component")
ax.set_ylabel("The fourth principal component")

"""### SPOT"""

pdf = pd.read_csv('/home/machine/Desktop/ML_Lab/Pizza.csv')
pdf.head()

pdf.dropna(inplace=True)

pdf['brand'] = pdf['brand'].map({'A': 1, 'B': 2, 'C': 3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10})

pdf['brand'][:5]

pdf = pdf.dropna(inplace=True)

pdf

pdf_shuffled = pdf.sample(frac=1, random_state=42)
pdf_shuffled.head()

pdf.isna()

pdf['brand'].isna().sum()

pdf.isna().sum()

plt.figure(figsize=(10,6))
plt.scatter(pdf['mois'],pdf['prot'],c=pdf['brand'],edgecolors='k',alpha=0.75,s=150)
plt.grid(True)
plt.title("Scatter plot of Moisture and Protein features showing their \ncorrelation and class seperation",fontsize=15)
plt.xlabel("Moisture",fontsize=15)
plt.ylabel("Protein",fontsize=15)
plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = pdf.drop('brand',axis=1)
X=scaler.fit_transform(X)

from sklearn.decomposition import PCA
pca = PCA()
final_piz = pca.fit_transform(X)  #performing eigen decomposition followed by projection

#displaying the variance captured by PCA
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

#Rounding off the variances to fewer decimal places
rounded_var=np.round(pca.explained_variance_,1)
plt.figure(figsize=(10,7))
pca_components = [i+1 for i in range(len(rounded_var))]
plt.scatter(pca_components,rounded_var,edgecolors='k',alpha=0.75,s=150)
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance obtained after PCA')
plt.title('Variance vs Component after PCA')
plt.xticks(np.arange(pca_components[0],pca_components[len(pca_components)-1]+1,1))
plt.show()

#Variance captured using first two principal components
var = np.sum(pca.explained_variance_[0:2])
print(np.round(var,2))
var_percentage = np.sum(pca.explained_variance_ratio_[0:2])*100
print(np.round(var_percentage,2),'%')

figure = plt.figure()
ax = plt.gca()
plt.scatter(final_piz[:,0],final_piz[:,1], c=pdf['brand'], edgecolor='none', alpha=0.5)
ax.set_title("The PCA plot")
ax.set_xlabel("The first principle component")
ax.set_ylabel("The second principle component")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('/home/machine/Desktop/ML_Lab/Pizza.csv')

# Display the first five rows
print(data.head())

# Remove the 'brand' and 'id' columns
data = data.drop(['brand', 'id'], axis=1)

# Scale the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Fit the PCA model
pca = PCA(n_components=7)
pca.fit(data_scaled)

# Compute the explained variance
explained_variance = pca.explained_variance_ratio_

# Plot the explained variance to determine the number of components
plt.plot(range(1, len(explained_variance) + 1), explained_variance * 100, marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Explained Variance (%)')
plt.title('Explained Variance vs. Number of Components')
plt.grid(True)
plt.show()

# (a) Number of components generated when running the analysis
num_components = len(pca.components_)
print(f'The PCA generated {num_components} components when first run.')

# (c) Number of components to keep
# Let's choose 3 components to maintain a reasonable trade-off between variance explained and model complexity
num_components_to_keep = 3

# Display the weight for each component
component_weights = pd.DataFrame(pca.components_, columns=['PC' + str(i) for i in range(1, len(pca.components_) + 1)])

print(component_weights)

# (b) Table of feature weights
print(f"\nFeature weights for each component:")
print(component_weights.round(3))

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("/home/machine/Desktop/ML_Lab/Pizza.csv")

# Separate features (nutritional values)
X = data.iloc[:, 2:].values

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA
pca = PCA()
pca.fit(X_scaled)

# a) Number of components generated
print("Number of components generated:", pca.n_components_)

# b) Feature weights for each component
component_weights = pd.DataFrame(pca.components_, columns=data.columns[2:])
print("\nFeature weights for each component:")
print(component_weights)

# c) Number of components to keep
# In real-world scenarios, you would use methods like explained variance ratio or scree plot to decide
# For demonstration, let's say we keep components that explain at least 90% of the variance
total_variance_ratio = pca.explained_variance_ratio_.cumsum()
num_components_to_keep = (total_variance_ratio >= 0.9).sum()
print("\nNumber of components to keep:", num_components_to_keep)

# d) Features to keep based on component weights and decision on the number of components
# Let's keep the features with highest absolute weights in the first 'num_components_to_keep' components
#features_to_keep = component_weights.abs().nlargest(num_components_to_keep, columns=data.columns[2:], keep='all')
#print("\nFeatures to keep based on component weights:")
#print(features_to_keep)
# Sum up all the columns


# Running PCA with reduced components
pca_reduced = PCA(n_components=num_components_to_keep)
X_pca_reduced = pca_reduced.fit_transform(X_scaled)

column_sums = component_weights.abs().sum()

# Find the column with the least sum
column_to_drop = column_sums.idxmin()

# Drop the column with the least sum
features_to_keep = component_weights.drop(columns=[column_to_drop])

print("\nFeatures to keep based on component weights ")
print(features_to_keep)

# Running PCA with reduced components
pca_reduced = PCA(n_components=num_components_to_keep)
X_pca_reduced = pca_reduced.fit_transform(X_scaled)

