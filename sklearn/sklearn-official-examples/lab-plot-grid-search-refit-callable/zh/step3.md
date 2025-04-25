# 加载数据并定义管道

我们将从 scikit-learn 中加载数字数据集，并定义一个由主成分分析（PCA）和线性支持向量分类器（LinearSVC）组成的管道。

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```
