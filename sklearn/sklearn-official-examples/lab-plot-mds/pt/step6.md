# Redimensionar e Girar os Dados

Em seguida, redimensionaremos e rotacionaremos os dados para visualização usando PCA do scikit-learn.

```python
# Redimensionar os dados
pos *= np.sqrt((X_true**2).sum()) / np.sqrt((pos**2).sum())
npos *= np.sqrt((X_true**2).sum()) / np.sqrt((npos**2).sum())

# Girar os dados
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)
pos = clf.fit_transform(pos)
npos = clf.fit_transform(npos)
```
