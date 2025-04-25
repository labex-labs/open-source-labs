# 创建绘图

在这一步中，我们将创建绘图。我们将使用`fig.text()`方法向绘图中添加文本。我们将遍历字体列表和相应的文本，使用`zip()`函数将它们匹配起来。我们将把`usetex`参数设置为`True`以启用 usetex 模式。

```python
fig = plt.figure()
for y, font, text in zip(
    range(5),
    ['ptmr8r', 'ptmri8r', 'ptmro8r', 'ptmr8rn', 'ptmrr8re'],
    [f'Nimbus Roman No9 L {x}'
     for x in ['', 'Italics (real italics for comparison)',
               '(slanted)', '(condensed)', '(extended)']],
):
    fig.text(.1, 1 - (y + 1) / 6, setfont(font) + text, usetex=True)

fig.suptitle('Usetex font effects')
plt.show()
```
