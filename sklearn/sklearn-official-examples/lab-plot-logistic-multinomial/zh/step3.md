# 训练多项式逻辑回归模型

现在我们将使用scikit-learn中的`LogisticRegression`函数训练一个多项式逻辑回归模型。我们将求解器设置为`sag`，最大迭代次数设置为100，随机数种子设置为42，多分类选项设置为`multinomial`。然后我们将打印模型的训练分数。

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
