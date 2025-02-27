# Lade die erforderlichen Bibliotheken und den MNIST-Datensatz

Der erste Schritt besteht darin, die erforderlichen Bibliotheken und den Datensatz zu laden. Wir werden die Bibliotheken `pandas`, `numpy`, `matplotlib` und `scikit-learn` verwenden. Wir werden auch die `fetch_openml`-Funktion aus scikit-learn verwenden, um den MNIST-Datensatz zu laden.

```python
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import shuffle

# Lade den MNIST-Datensatz
def load_mnist(n_samples=None, class_0="0", class_1="8"):
    """Lade MNIST, wähle zwei Klassen, mische und gib nur n_samples zurück."""
    # Lade Daten von http://openml.org/d/554
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="pandas")

    # Nimm nur zwei Klassen für die binäre Klassifizierung
    mask = np.logical_or(mnist.target == class_0, mnist.target == class_1)

    X, y = shuffle(mnist.data[mask], mnist.target[mask], random_state=42)
    if n_samples is not None:
        X, y = X[:n_samples], y[:n_samples]
    return X, y

X, y = load_mnist(n_samples=10000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
