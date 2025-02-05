# 创建分类器

我们将为每个 alpha 值创建 MLP 分类器。我们将创建一个管道，其中包括用于标准化数据的 StandardScaler 和具有不同 alpha 值的 MLPClassifier。我们将求解器设置为 'lbfgs'，它是拟牛顿法家族中的一种优化器。我们将 max_iter 设置为 2000，并将 early_stopping 设置为 True 以防止过拟合。我们将使用两个隐藏层，每个隐藏层有 10 个神经元。

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
