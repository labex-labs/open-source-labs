# 上側と右側の軸を非表示にする

ここでは、左側と下側の軸のみが必要なので、上側と右側の軸を非表示にします。

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```
