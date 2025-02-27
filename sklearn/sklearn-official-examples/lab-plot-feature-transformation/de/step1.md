# Datenvorbereitung

Zunächst erstellen wir einen großen Datensatz mit 80.000 Proben und teilen ihn in drei Mengen auf:

- Eine Menge, um die Ensemble-Methoden zu trainieren, die später als Feature-Engineering-Transformer verwendet werden
- Eine Menge, um das lineare Modell zu trainieren
- Eine Menge, um das lineare Modell zu testen.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=80_000, random_state=10)

X_full_train, X_test, y_full_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=10
)

X_train_ensemble, X_train_linear, y_train_ensemble, y_train_linear = train_test_split(
    X_full_train, y_full_train, test_size=0.5, random_state=10
)
```
