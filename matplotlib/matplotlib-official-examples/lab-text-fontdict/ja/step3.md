# プロットを作成する

さて、プロットを作成しましょう。NumPy を使ってデータを生成し、減衰する指数関数の減衰曲線を描画します。

```python
x = np.linspace(0.0, 5.0, 100)
y = np.cos(2*np.pi*x) * np.exp(-x)

plt.plot(x, y, 'k')
```
