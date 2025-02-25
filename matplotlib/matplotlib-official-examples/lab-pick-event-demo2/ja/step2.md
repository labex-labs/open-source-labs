# 平均と標準偏差の計算

次に、100のデータセットそれぞれの平均と標準偏差を計算します。これらの値を計算するために、numpyのmeanとstd関数を使用します。

```python
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
