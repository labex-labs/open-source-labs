# Construção do conjunto de dados

Neste passo, criaremos um conjunto de dados de classificação não linearmente separável composto por dois clusters de quantiles gaussianos utilizando a função `make_gaussian_quantiles` do módulo `sklearn.datasets`. Também concatenaremos os dois clusters e atribuiremos rótulos a eles.

```python
X1, y1 = make_gaussian_quantiles(
    cov=2.0, n_samples=200, n_features=2, n_classes=2, random_state=1
)
X2, y2 = make_gaussian_quantiles(
    mean=(3, 3), cov=1.5, n_samples=300, n_features=2, n_classes=2, random_state=1
)
X = np.concatenate((X1, X2))
y = np.concatenate((y1, -y2 + 1))
```
