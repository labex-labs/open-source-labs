# 2 番目のサブプロットに複数行のテキストを追加する

2 番目のサブプロットでは、`text`関数を使用して複数行のテキストを追加します。テキストの位置、サイズ、垂直および水平方向の配置、およびバウンディングボックスを指定できます。

```python
ax1.text(0.29, 0.4, "Mat\nTTp\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.34, 0.4, "Mag\nTTT\n123", size=18,
         va="baseline", ha="left", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.95, 0.4, "Mag\nTTT$^{A^A}$\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))
```
