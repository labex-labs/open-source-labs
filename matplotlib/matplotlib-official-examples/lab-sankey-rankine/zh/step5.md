# 添加标签和格式设置

我们将使用桑基图中每个补丁（patch）的 `text` 属性为其添加标签。我们还将把文本格式设置为加粗并增大字体大小。

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
