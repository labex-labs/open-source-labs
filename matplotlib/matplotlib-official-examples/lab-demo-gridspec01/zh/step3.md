# 使用 subplot2grid 定义子图

要使用 `subplot2grid` 定义子图，我们首先需要使用一个包含所需行数和列数的元组来指定网格的大小。我们还需要使用另一个元组来指定子图在网格中的位置。

例如，要创建一个 3x3 的网格，并在其中创建一个跨越整个第一行和所有三列的子图，我们使用以下代码：

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
```

要创建一个跨越第二行和前两列的子图，我们使用：

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
```

要创建一个跨越最后两行和最后一列的子图，我们使用：

```python
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
```

要在最后一行和第一列创建一个子图，我们使用：

```python
ax4 = plt.subplot2grid((3, 3), (2, 0))
```

要在最后一行和第二列创建一个子图，我们使用：

```python
ax5 = plt.subplot2grid((3, 3), (2, 1))
```
