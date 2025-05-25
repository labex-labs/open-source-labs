# Geração de Dados

Vamos gerar uma tarefa de classificação utilizando a função `make_classification` do scikit-learn. Vamos gerar 500 amostras com 15 recursos, dos quais 3 são informativos, 2 são redundantes e 10 são não informativos.

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```
