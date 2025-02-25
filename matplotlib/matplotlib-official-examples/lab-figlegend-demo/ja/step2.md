# 基本的なグラフを作成する

基本的なグラフを作成するには、x と y の値を定義し、それらを `plt.plot()` を使ってプロットする必要があります。ここでは、2 つのサイン波をプロットします。

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
