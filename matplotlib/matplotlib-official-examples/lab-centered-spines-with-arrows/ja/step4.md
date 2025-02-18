# 不要な軸を非表示にする

必要のない上と右の軸 (spine) も非表示にします。

```python
ax.spines[["top", "right"]].set_visible(False)
```
