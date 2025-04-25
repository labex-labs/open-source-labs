# 重新缩放和旋转数据

然后，我们将使用 scikit-learn 中的主成分分析（PCA）对数据进行重新缩放和旋转，以便进行可视化。

```python
# 重新缩放数据
pos *= np.sqrt((X_true**2).sum()) / np.sqrt((pos**2).sum())
npos *= np.sqrt((X_true**2).sum()) / np.sqrt((npos**2).sum())

# 旋转数据
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)
pos = clf.fit_transform(pos)
npos = clf.fit_transform(npos)
```
