# 添加文本水印

要添加文本水印，我们可以使用 `Figure` 对象的 `text()` 方法。我们需要提供位置、文本以及其他属性，如字体大小、颜色和透明度。

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```
