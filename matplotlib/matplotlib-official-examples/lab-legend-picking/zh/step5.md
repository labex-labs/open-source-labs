# 将图例线条映射到原始线条

我们将使用一个字典把图例线条映射到原始线条上。

```python
lines = [line1, line2]
lined = {}  # 用于将图例线条映射到原始线条。
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # 启用图例线条的选中功能。
    lined[legline] = origline
```
