# ラスタライズ付きで重ね合わせたテキスト付きの pcolormesh プロットを作成する

ラスタライズが、軸やテキストなどの一部のアーティストにとってベクトルグラフィックの利点を維持できる方法を示すために、ラスタライズ付きで重ね合わせたテキスト付きの pcolormesh プロットを作成します。

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
