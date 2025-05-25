# Carregar e Preparar Dados

Primeiro, carregaremos o conjunto de dados de diabetes e o prepararemos para modelagem. Usaremos a função `load_diabetes` do scikit-learn para carregar o conjunto de dados em dois arrays, `X` e `y`.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
