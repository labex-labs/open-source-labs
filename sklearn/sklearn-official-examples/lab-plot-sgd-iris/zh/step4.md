# 绘制训练点

现在我们将在决策面上绘制训练点。我们将使用 `scatter()` 方法为不同的目标值绘制不同颜色的训练点。

```python
for i, color in zip(clf.classes_, colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=color,
        label=iris.target_names[i],
        cmap=plt.cm.Paired,
        edgecolor="black",
        s=20,
    )
plt.title("Decision surface of multi-class SGD")
plt.axis("tight")
```
