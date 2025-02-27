# Lade den Iris-Datensatz

Wir werden den Iris-Datensatz aus der scikit-learn-Bibliothek laden. Der Datensatz enthält vier Merkmale: Kelchblattlänge, Kelchblattbreite, Blütenblattlänge und Blütenblattbreite. Wir werden nur die ersten beiden Merkmale für die binäre Klassifizierung verwenden.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 2] # Verwende nur die ersten beiden Merkmale für die binäre Klassifizierung
y = y[y!= 2]

X /= X.max() # Normalisiere X, um die Konvergenz zu beschleunigen
```
