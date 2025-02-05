# 带标题的标签

如果我们希望标签与标题对齐，可以将其合并到标题中，或者使用 `loc` 关键字参数。

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
