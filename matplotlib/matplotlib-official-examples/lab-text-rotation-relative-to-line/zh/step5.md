# 绘制正确旋转的文本

最后，我们将在考虑线条旋转的情况下，在指定位置绘制文本。这将使文本相对于线条以正确的角度旋转。

```python
# 绘制文本
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
