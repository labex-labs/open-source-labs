# ラスタライズ付きでpcolormeshプロットを作成する

ラスタライズがレンダリングを高速化し、ファイルサイズを小さくする方法を示すために、ラスタライズ付きでpcolormeshプロットを作成します。

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
