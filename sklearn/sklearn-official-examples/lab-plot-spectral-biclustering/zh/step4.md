# 绘制结果

现在，我们根据“谱双聚类（SpectralBiclustering）”模型分配的行和列标签，按升序重新排列数据，然后再次绘图。`row_labels_` 的范围是从0到3，而 `column_labels_` 的范围是从0到2，这表示每行共有4个聚类，每列共有3个聚类。

```python
# 先对行进行重新排序，然后对列进行重新排序。
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")
_ = plt.show()
```

作为最后一步，我们想要展示模型分配的行标签和列标签之间的关系。因此，我们使用 `numpy.outer` 创建一个网格，它接受排序后的 `row_labels_` 和 `column_labels_`，并给每个标签加1，以确保标签从1开始而不是0，以便更好地可视化。

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Checkerboard structure of rearranged data")
plt.show()
```
