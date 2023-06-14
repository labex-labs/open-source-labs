# Spectral Co-Clustering Algorithm

## Introduction

This lab demonstrates how to use the Spectral Co-Clustering algorithm to bicluster a dataset. The dataset is generated using the `make_biclusters` function, which creates a matrix of small values and implants biclusters with large values. The rows and columns are then shuffled and passed to the Spectral Co-Clustering algorithm. Rearranging the shuffled matrix to make biclusters contiguous shows how accurately the algorithm found the biclusters.

## Steps

### Step 1: Import necessary libraries

We need to import necessary libraries such as numpy, matplotlib, scikit-learn.

```python
import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import make_biclusters
from sklearn.cluster import SpectralCoclustering
from sklearn.metrics import consensus_score
```

### Step 2: Generate a dataset

We generate a dataset of shape (300, 300) with 5 biclusters and noise of 5 using `make_biclusters` function.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```

### Step 3: Visualize the original dataset

We visualize the original dataset using `matshow()` function.

```python
plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
```

### Step 4: Shuffle the dataset

We shuffle the dataset using `permutation()` function from numpy.

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```

### Step 5: Visualize the shuffled dataset

We visualize the shuffled dataset using `matshow()` function.

```python
plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled dataset")
```

### Step 6: Apply Spectral Co-Clustering algorithm

We apply Spectral Co-Clustering algorithm to shuffled dataset with 5 clusters.

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```

### Step 7: Calculate consensus score

We calculate the consensus score of biclusters using `consensus_score()` function.

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```

### Step 8: Rearrange the shuffled dataset

We rearrange the shuffled dataset to make the biclusters contiguous using `argsort()` function from numpy.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```

### Step 9: Visualize the biclusters

We visualize the biclusters using `matshow()` function.

```python
plt.matshow(fit_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")
```

## Summary

In this lab, we learned how to generate a dataset and bicluster it using the Spectral Co-Clustering algorithm. The original dataset was generated using the `make_biclusters` function, which created a matrix of small values and implanted biclusters with large values. We shuffled the rows and columns of the dataset and passed it to the Spectral Co-Clustering algorithm. We calculated the consensus score of the biclusters and rearranged the shuffled dataset to make the biclusters contiguous. Finally, we visualized the biclusters to show how accurately the algorithm found them.
