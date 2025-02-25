# 正弦波の線を作成する

デフォルトのカラーサイクルからの色を使って正弦波の線を作成します。

```python
# Create sinusoidal lines
L = 2*np.pi
x = np.linspace(0, L)
ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    plt.plot(x, np.sin(x + s), '-')
plt.margins(0)
plt.show()
```
