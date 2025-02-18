# Загрузка набора данных

Первый шаг — загрузить набор данных ирисов (iris dataset) из библиотеки scikit-learn.

```python
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
