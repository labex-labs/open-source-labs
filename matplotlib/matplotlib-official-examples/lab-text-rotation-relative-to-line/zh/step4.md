# 绘制未正确旋转的文本

现在我们将在不考虑线条旋转的情况下，在指定位置绘制文本。这将导致文本以 45 度角旋转，而这并非我们想要的效果。

```python
# 绘制文本
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
