# 平均と標準偏差の計算

次に、100 のデータセットそれぞれの平均と標準偏差を計算します。これらの値を計算するために、numpy の mean と std 関数を使用します。

```python
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
