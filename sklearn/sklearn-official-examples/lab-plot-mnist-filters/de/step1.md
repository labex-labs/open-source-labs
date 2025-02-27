# Bibliotheken importieren

Wir beginnen, indem wir die erforderlichen Bibliotheken für dieses Projekt importieren.

```python
import warnings
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
```