# 定义核函数

接下来，我们将定义核函数。在这个例子中，我们将使用径向基函数（RBF）核。我们将定义RBF核的两个版本：各向同性版本和各向异性版本。

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
