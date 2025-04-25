# 加载并准备数据

接下来，我们将加载并准备数据。我们会使用 scikit-learn 加载鸢尾花数据集，并仅选择两个特征。然后，我们会将数据拆分为训练集和测试集。

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# 我们只取两个特征。通过使用二维数据集，我们可以避免这种难看的切片操作
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
