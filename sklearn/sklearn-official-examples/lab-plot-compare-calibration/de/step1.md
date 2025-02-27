# Bibliotheken importieren und Dataset generieren

Wir beginnen mit dem Import der erforderlichen Bibliotheken und der Generierung eines synthetischen binären Klassifizierungsdatasets mit 100.000 Proben und 20 Merkmalen. Von den 20 Merkmalen sind nur 2 informativ, 2 sind redundant und die verbleibenden 16 sind uninformativ. Von den 100.000 Proben werden 100 zur Modellanpassung verwendet und der Rest zur Testung.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generate dataset
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # Samples used for training the models
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```
