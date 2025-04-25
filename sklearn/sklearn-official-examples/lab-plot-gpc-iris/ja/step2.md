# カーネル関数の定義

次に、カーネル関数を定義します。この例では、Radial Basis Function (RBF) カーネルを使用します。RBF カーネルの 2 つのバージョンを定義します。等方性バージョンと異方性バージョンです。

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
