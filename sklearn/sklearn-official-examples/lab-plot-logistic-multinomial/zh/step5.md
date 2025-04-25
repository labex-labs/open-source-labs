# 训练一对多逻辑回归模型

现在我们将使用与步骤 3 中相同的参数训练一个一对多逻辑回归模型，但多分类选项设置为`"ovr"`。然后我们将打印模型的训练分数。

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```
