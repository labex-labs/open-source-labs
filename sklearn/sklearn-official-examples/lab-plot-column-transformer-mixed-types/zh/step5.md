# 将分类器添加到预处理管道

在这一步中，我们将使用 `Pipeline` 将逻辑回归分类器添加到我们的预处理管道中。

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
