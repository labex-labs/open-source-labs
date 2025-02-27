# データの再スケーリングと回転

次に、scikit-learnのPCAを使って可視化のためにデータを再スケーリングと回転します。

```python
# データを再スケーリングする
pos *= np.sqrt((X_true**2).sum()) / np.sqrt((pos**2).sum())
npos *= np.sqrt((X_true**2).sum()) / np.sqrt((npos**2).sum())

# データを回転する
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)
pos = clf.fit_transform(pos)
npos = clf.fit_transform(npos)
```
