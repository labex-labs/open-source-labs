# 使用字典用任意字符串标记等高线

我们还可以使用字典用任意字符串标记等高线。这将使我们能够用自定义标签标记等高线。在这个例子中，我们将使用一个字符串列表来标记等高线。

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first','second', 'third', 'fourth', 'fifth','sixth','seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
