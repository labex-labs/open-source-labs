# 加载数据

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

加载并打乱`breast_cancer`数据集。然后我们将真实标签复制到`y_true`，并从`y`中移除前 50 个样本之外的所有标签。这将用于模拟半监督学习场景。
