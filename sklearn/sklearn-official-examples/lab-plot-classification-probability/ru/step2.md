# Загружаем датасет

Далее загружаем датасет iris из Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # we only take the first two features for visualization
y = iris.target
n_features = X.shape[1]
```
