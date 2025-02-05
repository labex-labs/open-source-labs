# 创建启用和平局决胜的支持向量机模型

在这一步中，我们将创建两个支持向量机（SVM）模型——一个禁用平局决胜，另一个启用平局决胜。我们将使用 scikit-learn 中的 `SVC` 类来创建这些模型。两个模型的 `break_ties` 参数分别设置为 `False` 和 `True`。

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```
