# 为半监督学习准备数据

我们选择 340 个样本，其中只有 40 个样本与已知标签相关联。我们存储另外 300 个样本的索引，这些样本的标签我们不应该知道。然后我们打乱标签，以便未标记的样本标记为 -1。

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```
