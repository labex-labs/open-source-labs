# Загружаем датасет

Далее, загрузим датасет, с которым будем работать. Для этого упражнения мы можем использовать любой датасет по своему выбору.

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Split the data into features and target
X = iris.data
y = iris.target
```
