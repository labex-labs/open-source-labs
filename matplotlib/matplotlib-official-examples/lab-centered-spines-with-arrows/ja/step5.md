# 軸の終端に矢印を描画する

軸の方向を示すために、軸 (spine) の終端に矢印を描画することができます。

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
