# 训练模型

我们将使用高斯过程分类（GPC）模型对数据进行分类。首先，我们需要指定核函数。

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

然后，我们可以创建一个 GPC 模型并使用数据对其进行训练。

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
