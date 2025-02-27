# Datenerzeugung

Wir werden eine Klassifizierungsaufgabe mit der `make_classification`-Funktion von scikit-learn erzeugen. Wir werden 500 Proben mit 15 Features erzeugen, von denen 3 informativ, 2 redundant und 10 nicht-informativ sind.

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
