# 定义用于存储结果的数组

```python
scores = np.empty((x_values.shape[0], n_splits))
amount_labeled = np.empty((x_values.shape[0], n_splits))
amount_iterations = np.empty((x_values.shape[0], n_splits))
```

我们定义数组来存储实验结果。
