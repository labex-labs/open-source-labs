# 获取数据集中第一个样本的类别概率

我们将获取数据集中第一个样本的类别概率，并将它们存储在 `class1_1` 和 `class2_1` 中。

```python
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]
```
