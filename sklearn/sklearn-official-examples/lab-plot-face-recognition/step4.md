# Perform PCA

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

We perform Principal Component Analysis (PCA) to extract features from the input data. We set the number of components to 150 and fit the PCA model to the training data. We then get the eigenfaces and transform the input data into principal components.


