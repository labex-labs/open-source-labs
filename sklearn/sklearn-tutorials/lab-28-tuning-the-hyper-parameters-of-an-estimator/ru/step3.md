# Определяем оценщик и сетку параметров

Теперь нам нужно определить оценщик, который мы хотим настроить, и сетку параметров, по которой мы хотим искать. Сетка параметров задает значения, которые мы хотим попробовать для каждого гиперпараметра.

```python
from sklearn.svm import SVC

# Create an instance of the support vector classifier
svc = SVC()

# Define the parameter grid
param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.1, 0.01, 0.001], 'kernel': ['linear', 'rbf']}
```
