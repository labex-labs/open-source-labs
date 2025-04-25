# ラスタライズなしで重ね合わせたテキスト付きの pcolormesh プロットを作成する

ベクトルグラフィックが、軸やテキストなどの一部のアーティストにとってベクトルグラフィックの利点を維持できる方法を示すために、ラスタライズなしで重ね合わせたテキスト付きの pcolormesh プロットを作成します。

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
