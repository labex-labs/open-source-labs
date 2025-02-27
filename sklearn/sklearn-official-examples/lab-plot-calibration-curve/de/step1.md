# Dataset

Wir werden einen synthetischen binären Klassifizierungsdatensatz mit 100.000 Proben und 20 Merkmalen verwenden. Von den 20 Merkmalen sind nur 2 informativ, 10 sind redundant (zufällige Kombinationen der informativen Merkmale) und die verbleibenden 8 sind nicht informativ (zufällige Zahlen). Von den 100.000 Proben werden 1.000 zur Modellanpassung verwendet und der Rest zur Testung.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=10, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.99, random_state=42
)
```
