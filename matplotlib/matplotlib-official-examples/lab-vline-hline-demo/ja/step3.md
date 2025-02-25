# データにノイズを追加する

このステップでは、データにいくらかのノイズを追加して、より現実的にするためにします。平均が 0.0 で標準偏差が 0.3 の乱数を生成するために、NumPy の `normal` 関数を使用します。

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
