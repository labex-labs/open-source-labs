# Den Datensatz laden und vorbereiten

Wir werden die scikit-learn-Bibliothek verwenden, um den Iris-Datensatz zu laden. Der Datensatz enthält 3 Klassen mit jeweils 50 Instanzen, wobei jede Klasse auf eine Art von Iris-Pflanze verweist. Jede Instanz hat 4 Merkmale: Kelchblattlänge, Kelchblattbreite, Blütenblattlänge und Blütenblattbreite.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# ladet den Iris-Datensatz
iris = datasets.load_iris()
X = iris.data[:, :2]  # wir nehmen nur die ersten beiden Merkmale.
Y = iris.target
```
