# 曲線を定義する

次に、誤差帯を描画する対象の曲線を定義します。この例では、パラメトリック曲線を使用します。パラメトリック曲線x(t), y(t)は、`~.Axes.plot`を使って直接描画できます。

```python
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)
```
