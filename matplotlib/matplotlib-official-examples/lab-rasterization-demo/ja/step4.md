# ラスタライズなしで pcolormesh プロットを作成する

ラスタライズと非ラスタライズの違いを示すために、ラスタライズなしで pcolormesh プロットを作成します。

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
