# 创建内部网格布局

现在，我们将创建内部网格布局。我们将使用 `GridSpecFromSubplotSpec` 方法来创建一个 3 行 3 列的网格布局，它将是外部网格布局的一个子图。

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
