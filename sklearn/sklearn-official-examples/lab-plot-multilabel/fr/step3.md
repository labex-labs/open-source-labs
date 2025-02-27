# Génération du jeu de données

Dans cette étape, nous générons le jeu de données à l'aide de la fonction `make_multilabel_classification` de `sklearn.datasets`.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
