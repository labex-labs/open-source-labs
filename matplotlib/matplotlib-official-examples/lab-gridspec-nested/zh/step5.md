# 创建另一个内部网格布局

现在我们将创建另一个内部网格布局。这次，我们将使用 `subgridspec` 方法来创建一个 3 行 3 列的网格布局，它将是外部网格布局第二列的一个子图。

```python
gs01 = gs0[1].subgridspec(3, 3)
```
