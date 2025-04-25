# 创建一个锚定偏移框

使用 AnnotationBbox 创建一个锚定偏移框，以添加偏移框并设置其位置。使用以下代码创建锚定偏移框：

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```
