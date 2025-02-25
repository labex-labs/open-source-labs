# 目盛りラベルの整列を調整する

最後に、`set_ha` と `set_va` メソッドを使って、目盛りラベルの水平および垂直方向の整列を調整できます。

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```
