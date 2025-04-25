# 基本的な使い方

`fill_between`関数は、2 つの線の間の領域を塗りつぶすために使用できます。パラメータの*y1*と*y2*はスカラー値でもよく、指定された y 値における水平境界を示します。*y1*のみが与えられた場合、*y2*の既定値は 0 になります。

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('fill between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('fill between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('fill between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()
```
