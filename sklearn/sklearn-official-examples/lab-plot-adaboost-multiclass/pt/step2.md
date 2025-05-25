# Carregar o Conjunto de Dados

Usaremos a função `make_gaussian_quantiles` de `sklearn.datasets` para gerar um conjunto de dados. Esta função gera distribuições gaussianas isotrópicas e adiciona separação entre as classes para tornar o problema mais difícil.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
