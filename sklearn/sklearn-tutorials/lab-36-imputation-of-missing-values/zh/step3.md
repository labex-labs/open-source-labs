# 使用IterativeImputer进行多变量特征插补

`IterativeImputer`类是一种用于插补缺失值的更高级方法。它将每个具有缺失值的特征建模为其他特征的函数，并使用该估计值进行插补。它会迭代地学习特征之间的关系，并根据这些关系插补缺失值。

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
