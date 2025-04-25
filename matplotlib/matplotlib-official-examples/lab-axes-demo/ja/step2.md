# データを生成する

このステップでは、プロットに使用するデータを生成します。NumPy の`convolve`関数を使ってガウス色ノイズを作成し、Matplotlib を使ってプロットします。

```python
np.random.seed(19680801)
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000] / 0.05)
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)] * dt

fig, main_ax = plt.subplots()
main_ax.plot(t, s)
```
