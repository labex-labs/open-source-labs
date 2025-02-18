# 画像を重ねる

プロット上に画像を重ねるには、`matplotlib.figure.Figure` クラスの `figimage` メソッドを使用できます。画像、プロット上の画像の位置、z オーダー（画像を前面に移動するため）、およびアルファ（画像を半透明にするため）を指定する必要があります。

```python
fig.figimage(im, 25, 25, zorder=3, alpha=.7)
```
