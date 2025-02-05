# 生成数据集

在这一步中，我们使用来自`sklearn.datasets`的`make_multilabel_classification`函数生成数据集。

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
