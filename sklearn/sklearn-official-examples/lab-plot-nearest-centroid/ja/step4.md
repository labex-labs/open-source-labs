# 分類器を作成して適合させる

収縮値0.2の最寄りの重心分類器のインスタンスを作成し、データに適合させます。

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```
