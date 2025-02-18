# 軸の枠線を非表示にする

ここでは、`ax1.spines.bottom.set_visible` と `ax2.spines.top.set_visible` を使用して、2 つのサブプロット間の軸の枠線（spine）を非表示にします。

```python
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
```
