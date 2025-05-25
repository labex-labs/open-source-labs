# Carregamento dos Dados

Carregamos o conjunto de dados de Diabetes do scikit-learn e imprimimos a sua descrição.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
