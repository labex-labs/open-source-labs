# Импортируем библиотеки и загружаем датасет

Начнем с импорта необходимых библиотек и загрузки датасета iris. Мы будем использовать функцию `load_iris` из модуля `sklearn.datasets` для загрузки датасета.

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable

print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of classes:", len(set(y)))
```
