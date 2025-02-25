# 対角線を描画する

まず、Matplotlib の `plot()` 関数を使って 45 度の対角線を描画します。

```python
fig, ax = plt.subplots()

# Plot diagonal line (45 degrees)
h = ax.plot(range(0, 10), range(0, 10))
```
