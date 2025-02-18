# Generieren von synthetischen Daten

Als Nächstes werden wir synthetische Daten generieren, um den Unterschied zwischen LDA und QDA zu demonstrieren. Wir verwenden die Funktion `make_classification` aus scikit-learn, um zwei Klassen mit unterschiedlichen Mustern zu erstellen.

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
