# ラスタライズなしでpcolormeshプロットを作成する

ラスタライズと非ラスタライズの違いを示すために、ラスタライズなしでpcolormeshプロットを作成します。

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
