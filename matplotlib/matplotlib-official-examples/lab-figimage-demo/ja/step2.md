# グラフと画像の作成

次に、配置したいグラフと画像を作成します。この例では、100x100 の乱数の配列を作成し、画像の右半分の値を 1 に設定します。その後、画像の 2 つの別々のインスタンスを作成し、それぞれ異なる位置と不透明度を持たせます。

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
