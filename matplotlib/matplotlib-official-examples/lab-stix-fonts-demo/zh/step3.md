# 绘制文本

既然我们已经定义了文本，就可以使用 Matplotlib 来绘制它。在这一步中，我们创建一个图形，并使用`fig.text()`方法将文本添加到其中。

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i +.5) / len(tests), s, fontsize=32)

plt.show()
```
