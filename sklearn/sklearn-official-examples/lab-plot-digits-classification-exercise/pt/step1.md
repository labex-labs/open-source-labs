# Carregar o conjunto de dados Digits

Começaremos carregando o conjunto de dados digits usando a função `load_digits` do scikit-learn. Esta função retorna dois arrays: `X_digits` contendo os dados de entrada e `y_digits` contendo as etiquetas alvo.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
