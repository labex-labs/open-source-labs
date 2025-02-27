# Определение функции ядра

Далее мы определим функцию ядра. В этом примере мы будем использовать ядро радиальной базисной функции (RBF). Мы определим две версии ядра RBF: изотропную и анизотропную.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
