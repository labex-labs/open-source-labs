# Comparison of LDA and PCA 2D Projection of Iris Dataset

## Introduction

In this lab, we will compare the performance of two popular dimensionality reduction algorithms, Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA), on the Iris dataset. The Iris dataset contains 3 types of Iris flowers with 4 attributes: sepal length, sepal width, petal length, and petal width.

## Steps

### Step 1: Load the Dataset

First, we need to load the Iris dataset using scikit-learn's built-in `load_iris()` function.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```

### Step 2: Perform PCA

Next, we will perform Principal Component Analysis (PCA) on the dataset to identify the combination of attributes that account for the most variance in the data. We will plot the different samples on the first two principal components.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Percentage of variance explained for each component
print("Explained variance ratio (first two components): %s" % str(pca.explained_variance_ratio_))

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA of Iris Dataset")
plt.show()
```

### Step 3: Perform LDA

Now, we will perform Linear Discriminant Analysis (LDA) on the dataset to identify attributes that account for the most variance between classes. Unlike PCA, LDA is a supervised method that uses known class labels.

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("LDA of Iris Dataset")
plt.show()
```

### Step 4: Compare Results

Finally, we will compare the results of PCA and LDA. We can see that LDA performs better than PCA in separating the three classes in the Iris dataset.

## Summary

In this lab, we learned how to perform Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA) on the Iris dataset using scikit-learn. We also compared the performance of these two dimensionality reduction algorithms and found that LDA performs better than PCA in separating the different classes in the dataset.
