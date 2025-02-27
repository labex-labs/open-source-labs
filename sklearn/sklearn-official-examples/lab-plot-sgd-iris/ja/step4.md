# 訓練ポイントをプロットする

ここでは、決定面上に訓練ポイントをプロットします。異なるターゲット値に対して異なる色で訓練ポイントをプロットするために、scatter()メソッドを使用します。

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
