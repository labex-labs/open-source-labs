# Preparar os Dados

Neste passo, prepararemos os conjuntos de dados sintéticos de classificação para a discretização de características. Usaremos a biblioteca scikit-learn para gerar três conjuntos de dados diferentes: luas, círculos concêntricos e dados linearmente separáveis.

```python
h = 0.02  # tamanho do passo na malha

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
