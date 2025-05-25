# Pré-processar os dados

Em seguida, pré-processaremos os dados escalando as características para um intervalo de [0, 1] usando o valor máximo dos dados. Isto pode ser feito dividindo os dados de entrada pelo valor máximo dos dados de entrada.

```python
X_digits = X_digits / X_digits.max()
```
