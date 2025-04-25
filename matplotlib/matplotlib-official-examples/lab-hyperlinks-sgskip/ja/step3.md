# ハイパーリンク付きの画像を作成する

このステップでは、画像を作成し、それにハイパーリンクを追加します。画像を作成するコードは次のとおりです。

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

画像にハイパーリンクを追加するには、画像オブジェクトの`set_url()`メソッドを使用します。このメソッドは、URL を引数として取ります。更新されたコードは次のとおりです。

```python
im.set_url('https://www.google.com/')
```

画像は`https://www.google.com/`へのハイパーリンクを持ちます。最後に、`fig.savefig()`を使用してプロットを SVG ファイルとして保存できます。

```python
fig.savefig('image.svg')
```
