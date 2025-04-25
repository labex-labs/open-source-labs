# 创建带有超链接的散点图

在这一步中，我们将创建一个散点图，并为标记添加超链接。以下是创建散点图的代码：

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

要添加超链接，我们需要使用散点图对象的 `set_urls()` 方法。此方法将 URL 列表作为其参数。以下是更新后的代码：

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

前两个标记将分别具有指向 `https://www.bbc.com/news` 和 `https://www.google.com/` 的超链接。第三个标记将没有超链接。最后，我们可以使用 `fig.savefig()` 将图表保存为 SVG 文件：

```python
fig.savefig('scatter.svg')
```
