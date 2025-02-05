# 创建另一个文本框

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

我们创建了另一个包含单词“spam”的文本框。这次我们将 `boxstyle` 参数设置为“square”以创建一个方形框，并将 `ha` 和 `va` 参数设置为“right”和“top”，以便将文本对齐到框的右侧和顶部。
