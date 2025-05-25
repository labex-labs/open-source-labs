# Geração de dados aleatórios

Vamos gerar dados aleatórios com a função `make_regression` do scikit-learn. Definiremos `n_samples` para 10, `n_features` para 10 e `random_state` para 1. Esta função retornará as nossas características de entrada X, a variável alvo y e os valores verdadeiros dos coeficientes w.

```python
X, y, w = make_regression(
    n_samples=10, n_features=10, coef=True, random_state=1, bias=3.5
)
```
