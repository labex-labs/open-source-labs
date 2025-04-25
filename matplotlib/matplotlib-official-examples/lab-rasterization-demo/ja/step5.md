# ラスタライズ付きで pcolormesh プロットを作成する

ラスタライズがレンダリングを高速化し、ファイルサイズを小さくする方法を示すために、ラスタライズ付きで pcolormesh プロットを作成します。

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
