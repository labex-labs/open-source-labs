# プロット用のデータ作成

このステップでは、コントーアプロットにプロットするデータを作成します。`np.meshgrid()`関数を使用して点のグリッドを作成し、その後、サイン関数とコサイン関数を使用して`z`値を計算します。

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
