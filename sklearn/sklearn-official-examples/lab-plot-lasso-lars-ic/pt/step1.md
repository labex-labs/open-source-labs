# Carregar os Dados

Carregaremos o conjunto de dados de diabetes do scikit-learn usando o método `load_diabetes`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
