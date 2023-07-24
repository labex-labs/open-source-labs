# Non-negative Matrix Factorization (NMF)

#### NMF with the Frobenius norm

Non-negative Matrix Factorization (NMF) is an alternative approach to decomposition that assumes non-negative data and components. It finds a decomposition of the data into two matrices of non-negative elements by optimizing the distance between the data and the matrix product of the two matrices. NMF can be implemented using the `NMF` class from scikit-learn.

```python
from sklearn.decomposition import NMF

# Create an NMF object with n_components as the number of desired components
nmf = NMF(n_components=2)

# Fit the NMF model to the data
nmf.fit(data)

# Decompose the data into the two non-negative matrices
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```
