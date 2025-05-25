# Gerar Conjunto de Dados

Neste passo, geramos o conjunto de dados utilizando a função `make_multilabel_classification` de `sklearn.datasets`.

```python
X, Y = make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1
)
```
