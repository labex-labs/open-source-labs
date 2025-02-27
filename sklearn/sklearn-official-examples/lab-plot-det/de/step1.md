# Synthetische Daten generieren

Wir werden die Funktion `make_classification` von scikit - learn verwenden, um synthetische Daten zu generieren. Diese Funktion erzeugt ein zufälliges n - Klassifikationsproblem mit n_informative informativen Merkmalen, n_redundant redundanten Merkmalen und n_clusters_per_class Clustern pro Klasse. Wir werden 1000 Proben mit 2 informativen Merkmalen und einem Zufallszustand von 1 generieren. Anschließend teilen wir die Daten in Trainings - und Testsets im Verhältnis 60/40 auf.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
