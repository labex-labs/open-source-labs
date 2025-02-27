# Lade den Datensatz

Wir werden einen Datensatz aus zwei geschachtelten Kreisen mit der Funktion `make_circles` aus `sklearn.datasets` erstellen.

```python
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
