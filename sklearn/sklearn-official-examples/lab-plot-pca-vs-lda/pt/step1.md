# Carregar o Conjunto de Dados

Primeiro, precisamos carregar o conjunto de dados Iris usando a função `load_iris()` integrada do scikit-learn.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```
